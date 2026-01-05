## A simplified sketch of the ELIZA algorithm. The power of the transform comes from the particular transfroms associated with eack keyword.
**ELIZA is a chatbot that is used in early days in psycholog, where the patients chat with the robot**.

ELIZA_GENERATOR(sentence) → response

Find all keywords w in sentence

IF at least one keyword is found THEN
    Let w be the highest-ranked matching keyword
    Choose a transformation rule r associated with w
    response ← Apply r to sentence

    IF w = "my" AND r has a memory transformation THEN
        future ← Apply memory transformation to sentence
        Push future onto memory stack
ELSE
    IF memory stack is not empty AND randomly chosen THEN
        response ← Pop top item from memory stack
    ELSE
        response ← Apply NONE rule to sentence

RETURN response
