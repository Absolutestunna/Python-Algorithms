#Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.

#Memory conservation. In the specific case of iterating through large data, it's better to use a generator becauase gens iterate on its current state (after being "paused" from the last state). It has a memory of the last iterate and continues on that state when the func is called
