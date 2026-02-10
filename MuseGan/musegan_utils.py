import os
import numpy as np
import music21
import matplotlib.pyplot as plt


# --------------------------------------------------
# Convert soft piano-roll output to discrete pitches
# --------------------------------------------------
def binaries_output(output):
    """
    output shape:
    [batch_size, n_bars, n_steps_per_bar, n_pitches, n_tracks]
    """
    return np.argmax(output, axis=3)


# --------------------------------------------------
# Convert generated piano roll to MIDI files
# --------------------------------------------------
def notes_to_midi(output, n_bars, n_tracks, n_steps_per_bar, filename):
    os.makedirs("output", exist_ok=True)

    max_pitches = binaries_output(output)

    for score_num in range(len(output)):
        midi_note_score = max_pitches[score_num].reshape(
            [n_bars * n_steps_per_bar, n_tracks]
        )

        score = music21.stream.Score()
        score.append(music21.tempo.MetronomeMark(number=66))

        for track in range(n_tracks):
            part = music21.stream.Part()
            last_pitch = int(midi_note_score[0, track])
            duration = 0.0

            for idx, pitch in enumerate(midi_note_score[:, track]):
                pitch = int(pitch)

                if pitch != last_pitch and idx > 0:
                    note = music21.note.Note(last_pitch)
                    note.duration = music21.duration.Duration(duration)
                    part.append(note)
                    duration = 0.0

                last_pitch = pitch
                duration += 0.25

            # add final note
            note = music21.note.Note(last_pitch)
            note.duration = music21.duration.Duration(duration)
            part.append(note)

            score.append(part)

        score.write(
            "midi",
            fp=f"./output/{filename}_{score_num}.midi"
        )


# --------------------------------------------------
# Draw a single bar of a score
# --------------------------------------------------
def draw_bar(data, score_num, bar, track):
    plt.imshow(
        data[score_num, bar, :, :, track].transpose([1, 0]),
        origin="lower",
        cmap="Greys",
        vmin=-1,
        vmax=1,
    )
    plt.xlabel("Time")
    plt.ylabel("Pitch")


# --------------------------------------------------
# Draw full score (all bars & tracks)
# --------------------------------------------------
def draw_score(data, score_num):
    n_bars = data.shape[1]
    n_tracks = data.shape[-1]

    fig, axes = plt.subplots(
        nrows=n_tracks,
        ncols=n_bars,
        figsize=(12, 8),
        sharex=True,
        sharey=True
    )

    if n_tracks == 1:
        axes = np.expand_dims(axes, axis=0)
    if n_bars == 1:
        axes = np.expand_dims(axes, axis=1)

    for bar in range(n_bars):
        for track in range(n_tracks):
            axes[track, bar].imshow(
                data[score_num, bar, :, :, track].transpose([1, 0]),
                origin="lower",
                cmap="Greys"
            )
            axes[track, bar].set_xticks([])
            axes[track, bar].set_yticks([])

    plt.tight_layout()
    plt.show()
