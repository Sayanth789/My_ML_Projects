**Beam search** is a heuristic algorithm used in AI and Machine Learning to find the most likely
sequecnce  by exploring a limited number of the most promising options at each step.

 It is a variant of best first search that avoids the computational cost of exploring all possible 
 paths by keeping a fixed number of candidates, called "beam width". This makes it more effifcient 
 than an exhaustive search for problems with a very large  state space, such as machine translation
 or speech recognition.


function BEAMSEARCH(c, beam_width) returns best_paths
  y0, h0 ← 0
  path ← ()
  complete_paths ← ∅


 state ← (c, y0, h0, path)
 frontier ← { state } // initial frontier

 
 while frontier contains incomplete paths do
   extended_frontier ← ∅
     for each state ∈ frontier do
       successor ← NEWSTATE(state, i, v_i)
         extended_frontier ← ADDTOBEAM(
                                     successor,
                                     extended_frontier,
                                     beam_width
                                     )
                                     

     for each state ∈ extended_frontier do
      if state_is_complete(state) then
        complete_paths ← APPEND(complete_paths, state)
        extended_frontier ← REMOVE(extended_frontier, state)


    frontier ← extended_frontier


  return complete_paths      

function NEWSTATE(state, word, word_prob) 
   return new_state 
   
     
// BEAM maintanance ...................

function ADDTOBEAM(state, frontier, width) 
     if LENGTH(frontier) < width then 
         frontier <- INSERT(state, frontier)

     else if SCORE(state) > SCORE(WORSTOF(frontier)) then 
         frontier <- REMOVE(frontier)
         frontier <- INSERT(state, frontier) 

     return frontier 
         
 
 ###  How it works 

 * At each step: The algorithm generates all possible next options from the current set of candidates.
 * Evaluates options: It evaluates these new options based on a heuristic function (eg: the probability of
 * a sequence)

 * Prunes the search : It selects only the top-ranked options, determined by the "beam width" (a pre
defined number ) and discards the rest
* Continues : This process repeats, expanding the remaning candidates untill a goal state is reached .

* ### Key characteristics
* Beam Width : This parameter controls the trade-off between accuracy and computational efficiency.
*  A larger beam width uses more memory and time but has a higher chance of finding a better solution,
  while a smaller width is faster but might miss the optimal path.

* Heuristic nature : Because it doesnot explore all paths , beam search is not guaranteed to find the glo
 bally optimal solutions

* Efficiency : it is significantly more memory effiecient than an exhaustive search, making it practical
 for complex problems.

* Approximation :  It provides a good approximation of the optimal solution by balancing explorations and
* efficiency, making it widely used in applications like natural language processing and speech recognition
   

