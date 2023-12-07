

# CMPS 2200 Assignment 1

**Name:**_________zoe ________________


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answers will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your GitHub repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
true since 2n^n+1 = 2 *2^n pick c ?= and n(0) = 0.  
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  no, it is not in O(2^n). raising the power of 2n means the growth rate is much faster than 2^n which is a single exponential function. Using limitis you can see this to be true. Seeing that the limit is not a constant but grows as n increases as well means that 2^(2N) grows much further than 2^n 
.  
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  
.  no  $n^{1.01} is not in O(\mathrm{log}^2 n)$. in this case n^1.101 is a polynomial function and has a faster growth rate than the log one. Showing this by using the limit of the ration between them as it approaches infinity shows that it is not finite. Using the limit of infinity shows that n ^1.1001 grows much faster. 
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  
.   $n^{1.01} is in omega(log^2 n). setting the limit to infinity shows that n^1.101 grow much faster than log(2n) which we looked at before but being in a omega g(n))) function the f(n) grows at6 least as fast as the larger values of n making it grow least as fast as the square of the log 
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  the square root of n is not in O(log)^3) the square root itself has a slower growth rate than polynomial function of the log
.  
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
Yes from the prevois question 

2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.   def foo(x0:
    if x <= 1:
    return x
  else:
ra = foo(x-1)
rb = foo(x -2)
return ra + rb
.  
.  
.  
.  this function uses the func food to calculate and return a fibonacci number n. if x is less than or equal to 1 it returns x itself. if x is greater than 1 using recursion it calcualtes fibonacci number going through ra and rb til the robinacci nuymber is generated 
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  def longest_run(my array, key):
for num in myarrya:
if num == key:
current_run += 1
else:
if current_run > max:
max = current_run
current_run = -

if current_run > max_run:
max = current_run

return max
.  
.  
.  the work and span for this func longest_run. the work is )(n) because the work is proportial to length of the "my array". span is also O(n) because there is not parrellism 
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  
.  the work and span is O(n) because the work is proportional to the length of thr array. The span however is O(log n) because of the two recursion calls the algorthm combines the calls resulting in the span being that
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  if we do this in a similar way the work would still end up being O(n) because the basic operations prefromed and each recursive call is apart of the array. the span will be also O(log n) becdause of the recurison tree.
.  
.  
.  
.  
.  
.  
.  

