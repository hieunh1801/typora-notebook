![Python Timer Functions: Three Ways to Monitor Your Code](Python%20timm34.assets/Three-Ways-to-Time-Your-Code_Watermarked.8d561fcc7a35.jpg)

# Python Timer Functions: Three Ways to Monitor Your Code

by [Geir Arne Hjelle](https://realpython.com/python-timer/#author) Dec 30, 2019 [9 Comments](https://realpython.com/python-timer/#reader-comments) [intermediate](https://realpython.com/tutorials/intermediate/) [python](https://realpython.com/tutorials/python/)

[Tweet](https://twitter.com/intent/tweet/?text=Check out this %23Python tutorial: Python Timer Functions%3A Three Ways to Monitor Your Code by @realpython&url=https%3A//realpython.com/python-timer/) [Share](https://facebook.com/sharer/sharer.php?u=https%3A//realpython.com/python-timer/) [Email](mailto:?subject=Python article for you&body=Check out this Python tutorial: Python Timer Functions%3A Three Ways to Monitor Your Code https%3A//realpython.com/python-timer/)



Table of Contents

- Python Timers
  - [Python Timer Functions](https://realpython.com/python-timer/#python-timer-functions)
  - [Example: Download Tutorials](https://realpython.com/python-timer/#example-download-tutorials)
  - [Your First Python Timer](https://realpython.com/python-timer/#your-first-python-timer)
- A Python Timer Class
  - [Understanding Classes in Python](https://realpython.com/python-timer/#understanding-classes-in-python)
  - [Creating a Python Timer Class](https://realpython.com/python-timer/#creating-a-python-timer-class)
  - [Using the Python Timer Class](https://realpython.com/python-timer/#using-the-python-timer-class)
  - [Adding More Convenience and Flexibility](https://realpython.com/python-timer/#adding-more-convenience-and-flexibility)
- A Python Timer Context Manager
  - [Understanding Context Managers in Python](https://realpython.com/python-timer/#understanding-context-managers-in-python)
  - [Creating a Python Timer Context Manager](https://realpython.com/python-timer/#creating-a-python-timer-context-manager)
  - [Using the Python Timer Context Manager](https://realpython.com/python-timer/#using-the-python-timer-context-manager)
- A Python Timer Decorator
  - [Understanding Decorators in Python](https://realpython.com/python-timer/#understanding-decorators-in-python)
  - [Creating a Python Timer Decorator](https://realpython.com/python-timer/#creating-a-python-timer-decorator)
  - [Using the Python Timer Decorator](https://realpython.com/python-timer/#using-the-python-timer-decorator)
- [The Python Timer Code](https://realpython.com/python-timer/#the-python-timer-code)
- Other Python Timer Functions
  - [Using Alternative Python Timer Functions](https://realpython.com/python-timer/#using-alternative-python-timer-functions)
  - [Estimating Running Time With timeit](https://realpython.com/python-timer/#estimating-running-time-with-timeit)
  - [Finding Bottlenecks in Your Code With Profilers](https://realpython.com/python-timer/#finding-bottlenecks-in-your-code-with-profilers)
- [Conclusion](https://realpython.com/python-timer/#conclusion)
- [Resources](https://realpython.com/python-timer/#resources)

[![img](Python%20timm34.assets/a49ca0f23f17e4826bfc71fde2d72a30.png)](https://srv.realpython.net/click/5815603782/?c=43766333882&p=58946116052&r=93292)

While many developers [recognize](https://www.python.org/doc/essays/blurb/) Python as an effective programming language, pure Python programs may [run slower](https://www.ibm.com/developerworks/community/blogs/jfp/entry/A_Comparison_Of_C_Julia_Python_Numba_Cython_Scipy_and_BLAS_on_LU_Factorization) than their counterparts in compiled languages like C, Rust, and Java. Throughout this tutorial, you’ll see how to use a **Python timer** to monitor how fast your programs are running.

**In this tutorial, you’ll learn how to use:**

- **`time.perf_counter()`** to measure time in Python
- **Classes** to keep state
- **Context managers** to work with a block of code
- **Decorators** to customize a function

You’ll also gain background knowledge into how classes, context managers, and decorators work. As you see examples of each concept, you’ll be inspired to use one or several of them in your code, both for timing code execution and other applications. Each method has its advantages, and you’ll learn which to use depending on the situation. Plus, you’ll have a working Python timer that you can use to monitor your programs!

**Decorators Q&A Transcript:** [Click here to get access to a 25-page chat log from our recent Python decorators Q&A session](https://realpython.com/bonus/decorators-qa-2019/) in the Real Python Community Slack where we discussed common decorator questions.



## Python Timers

First, you’ll take a look at some example code that you’ll use throughout the tutorial. Later, you’ll add a **Python timer** to this code to monitor its performance. You’ll also see some of the simplest ways to measure the running time of this example.

### Python Timer Functions

If you look at the built in [`time`](https://docs.python.org/3/library/time.html) module in Python, then you’ll notice several functions that can measure time:

- [`monotonic()`](https://docs.python.org/3/library/time.html#time.monotonic)
- [`perf_counter()`](https://docs.python.org/3/library/time.html#time.perf_counter)
- [`process_time()`](https://docs.python.org/3/library/time.html#time.process_time)
- [`time()`](https://docs.python.org/3/library/time.html#time.time)

[Python 3.7](https://realpython.com/python37-new-features/) introduced several new functions, like [`thread_time()`](https://docs.python.org/3/library/time.html#time.thread_time), as well as **nanosecond** versions of all the functions above, named with an `_ns` suffix. For example, [`perf_counter_ns()`](https://docs.python.org/3/library/time.html#time.perf_counter_ns) is the nanosecond version of `perf_counter()`. You’ll learn more about these functions later. For now, note what the documentation has to say about `perf_counter()`:

> Return the value (in fractional seconds) of a performance counter, i.e. a clock with the highest available resolution to measure a short duration. ([Source](https://docs.python.org/3/library/time.html#time.perf_counter))

First, you’ll use `perf_counter()` to create a Python timer. [Later](https://realpython.com/python-timer/#other-python-timer-functions), you’ll compare this with other Python timer functions and learn why `perf_counter()` is usually the best choice.

### Example: Download Tutorials

To better compare the different ways you can add a Python timer to your code, you’ll apply different Python timer functions to the same code example throughout this tutorial. If you already have code you’d like to measure, then feel free to follow the examples with that instead.

The example you’ll see in this tutorial is a short function that uses the [`realpython-reader`](https://pypi.org/project/realpython-reader/) package to download the latest tutorials available here on *Real Python*. To learn more about the Real Python Reader and how it works, check out [How to Publish an Open-Source Python Package to PyPI](https://realpython.com/pypi-publish-python-package/). You can install `realpython-reader` on your system with [`pip`](https://realpython.com/what-is-pip/):

```
$ python -m pip install realpython-reader
```

Then, you can import the package as `reader`.

You’ll store the example in a file named `latest_tutorial.py`. The code consists of one function that downloads and prints the latest tutorial from *Real Python*:

```python
 1 # latest_tutorial.py
 2 
 3 from reader import feed
 4 
 5 def main():
 6     """Download and print the latest tutorial from Real Python"""
 7     tutorial = feed.get_article(0)
 8     print(tutorial)
 9 
10 if __name__ == "__main__":
11     main()
```

`realpython-reader` handles most of the hard work:

- **Line 3** imports `feed` from `realpython-reader`. This module contains functionality for downloading tutorials from the [*Real Python* feed](https://realpython.com/contact/#rss-atom-feed).
- **Line 7** downloads the latest tutorial from *Real Python*. The number `0` is an offset, where `0` means the most recent tutorial, `1` is the previous tutorial, and so on.
- **Line 8** prints the tutorial to the console.
- **Line 11** calls `main()` when you run the script.

When you run this example, your output will typically look something like this:

```
$ python latest_tutorial.py
# Python Timer Functions: Three Ways to Monitor Your Code

While many developers recognize Python as an effective programming language,
pure Python programs may run slower than their counterparts in compiled
languages like C, Rust, and Java. Throughout this tutorial, you’ll see how to
use a Python timer to monitor how fast your programs are running.

[ ... The full text of the tutorial ... ]
```

The code may take a little while to run depending on the network, so you might want to use a Python timer to monitor the performance of the script.

### Your First Python Timer

Let’s add a bare-bones Python timer to the example with `time.perf_counter()`. Again, this is a **performance counter** that’s well-suited for timing parts of your code.

`perf_counter()` measures the time in seconds from some unspecified moment in time, which means that the return value of a single call to the function isn’t useful. However, when you look at the difference between two calls to `perf_counter()`, you can figure out how many seconds passed between the two calls:

\>>>

```
>>> import time
>>> time.perf_counter()
32311.48899951

>>> time.perf_counter()  # A few seconds later
32315.261320793
```

In this example, you made two calls to `perf_counter()` almost 4 seconds apart. You can confirm this by calculating the difference between the two outputs: 32315.26 - 32311.49 = 3.77.

You can now add a Python timer to the example code:

```
 1 # latest_tutorial.py
 2 
 3 import time
 4 from reader import feed
 5 
 6 def main():
 7     """Print the latest tutorial from Real Python"""
 8     tic = time.perf_counter()
 9     tutorial = feed.get_article(0)
10     toc = time.perf_counter()
11     print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")
12 
13     print(tutorial)
14 
15 if __name__ == "__main__":
16     main()
```

Note that you call `perf_counter()` both before and after downloading the tutorial. You then print the time it took to download the tutorial by calculating the difference between the two calls.

**Note:** In line 11, the `f` before the string indicates that this is an **f-string**, which is a convenient way to format a text string. `:0.4f` is a format specifier that says the number, `toc - tic`, should be printed as a decimal number with four decimals.

f-strings are only available in Python 3.6 and later. For more information, check out [Python 3’s f-Strings: An Improved String Formatting Syntax](https://realpython.com/python-f-strings/).

Now, when you run the example, you’ll see the elapsed time before the tutorial:

```
$ python latest_tutorial.py
Downloaded the tutorial in 0.67 seconds
# Python Timer Functions: Three Ways to Monitor Your Code

[ ... The full text of the tutorial ... ]
```

That’s it! You’ve covered the basics of timing your own Python code. In the rest of the tutorial, you’ll learn how you can wrap a Python timer into a class, a context manager, and a decorator to make it more consistent and convenient to use.

## A Python Timer Class

Look back at how you added the Python timer to the example above. Note that you need at least one variable (`tic`) to store the state of the Python timer before you download the tutorial. After staring at the code a little, you might also note that the three highlighted lines are added only for timing purposes! Now, you’ll create a class that does the same as your manual calls to `perf_counter()`, but in a more readable and consistent manner.

Throughout this tutorial, you’ll create and update `Timer`, a class that you can use to time your code in several different ways. The final code is also available on [PyPI](https://pypi.org/project/codetiming) under the name `codetiming`. You can install this to your system like so:

```
$ python -m pip install codetiming
```

You can find more information about `codetiming` later on in this tutorial, in the section named [The Python Timer Code](https://realpython.com/python-timer/#the-python-timer-code).

### Understanding Classes in Python

**Classes** are the main building blocks of [object-oriented programming](https://realpython.com/courses/intro-object-oriented-programming-oop-python/). A **class** is essentially a template that you can use to create **objects**. While Python doesn’t force you to program in an object-oriented manner, classes are everywhere in the language. For a quick proof, let’s investigate the `time` module:

\>>>

```
>>> import time
>>> type(time)
<class 'module'>

>>> time.__class__
<class 'module'>
```

`type()` returns the type of an object. Here you can see that modules are in fact objects created from a `module` class. The special attribute `.__class__` can be used to get access to the class that defines an object. In fact, almost everything in Python is a class:

\>>>

```
>>> type(3)
<class 'int'>

>>> type(None)
<class 'NoneType'>

>>> type(print)
<class 'builtin_function_or_method'>

>>> type(type)
<class 'type'>
```

In Python, classes are great when you need to model something that needs to keep track of a particular state. In general, a class is a collection of properties (called **attributes**) and behaviors (called **methods**). For more background on classes and object-oriented programming, check out [Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/) or the [official docs](https://docs.python.org/3/tutorial/classes.html).

### Creating a Python Timer Class

Classes are good for tracking **state**. In a `Timer` class, you want to keep track of when a timer starts and how much time has passed since then. For the first implementation of `Timer`, you’ll add a `._start_time` attribute, as well as `.start()` and `.stop()` methods. Add the following code to a file named `timer.py`:

```
 1 # timer.py
 2 
 3 import time
 4 
 5 class TimerError(Exception):
 6     """A custom exception used to report errors in use of Timer class"""
 7 
 8 class Timer:
 9     def __init__(self):
10         self._start_time = None
11 
12     def start(self):
13         """Start a new timer"""
14         if self._start_time is not None:
15             raise TimerError(f"Timer is running. Use .stop() to stop it")
16 
17         self._start_time = time.perf_counter()
18 
19     def stop(self):
20         """Stop the timer, and report the elapsed time"""
21         if self._start_time is None:
22             raise TimerError(f"Timer is not running. Use .start() to start it")
23 
24         elapsed_time = time.perf_counter() - self._start_time
25         self._start_time = None
26         print(f"Elapsed time: {elapsed_time:0.4f} seconds")
```

A few different things are happening here, so let’s walk through the code step by step.

In line 5, you define a `TimerError` class. The `(Exception)` notation means that `TimerError` **inherits** from another class called `Exception`. Python uses this built-in class for error handling. You don’t need to add any attributes or methods to `TimerError`. However, having a custom error will give you more flexibility to handle problems inside `Timer`. For more information, check out [Python Exceptions: An Introduction](https://realpython.com/python-exceptions/).

The definition of `Timer` itself starts on line 8. When you first create or **instantiate** an object from a class, your code calls the special method `.__init__()`. In this first version of `Timer`, you only initialize the `._start_time` attribute, which you’ll use to track the state of your Python timer. It has the value `None` when the timer isn’t running. Once the timer is running, `._start_time` keeps track of when the timer started.

**Note:** The [underscore](https://namingconvention.org/python/underscore.html) prefix of `._start_time` is a Python convention. It signals that `._start_time` is an internal attribute that should not be manipulated by users of the `Timer` class.

When you call `.start()` to start a new Python timer, you first check that the timer isn’t already running. Then you store the current value of `perf_counter()` in `._start_time`. On the other hand, when you call `.stop()`, you first check that the Python timer is running. If it is, then you calculate the elapsed time as the difference between the current value of `perf_counter()` and the one you stored in `._start_time`. Finally, you reset `._start_time` so that the timer can be restarted, and print the elapsed time.

Here’s how you use `Timer`:

\>>>

```
>>> from timer import Timer
>>> t = Timer()
>>> t.start()

>>> t.stop()  # A few seconds later
Elapsed time: 3.8191 seconds
```

Compare this to the [earlier example](https://realpython.com/python-timer/#your-first-python-timer) where you used `perf_counter()` directly. The structure of the code is fairly similar, but now the code is more clear, and this is one of the benefits of using classes. By carefully choosing your class, method, and attribute names, you can make your code very descriptive!

### Using the Python Timer Class

Let’s apply `Timer` to `latest_tutorial.py`. You only need to make a few changes to your previous code:

```
# latest_tutorial.py

from timer import Timer
from reader import feed

def main():
    """Print the latest tutorial from Real Python"""
    t = Timer()
    t.start()
    tutorial = feed.get_article(0)
    t.stop()

    print(tutorial)

if __name__ == "__main__":
    main()
```

Notice that the code is very similar to what you saw earlier. In addition to making the code more readable, `Timer` takes care of printing the elapsed time to the console, which makes the logging of time spent more consistent. When you run the code, you’ll see pretty much the same output:

```
$ python latest_tutorial.py
Elapsed time: 0.64 seconds
# Python Timer Functions: Three Ways to Monitor Your Code

[ ... The full text of the tutorial ... ]
```

Printing the elapsed time from `Timer` may be consistent, but it seems that this approach is not very flexible. In the next section, you’ll see how to customize your class.

### Adding More Convenience and Flexibility

So far, you’ve seen that classes are suitable for when you want to encapsulate state and ensure consistent behavior in your code. In this section, you’ll add more convenience and flexibility to your Python timer:

- **Use** adaptable text and formatting when reporting the time spent
- **Apply** flexible logging, either to the screen, to a log file, or other parts of your program
- **Create** a Python timer that can accumulate over several invocations
- **Build** an informative representation of a Python timer

First, let’s see how you can customize the text used to report the time spent. In the previous code, the text `f"Elapsed time: {elapsed_time:0.4f} seconds"` is hard-coded into `.stop()`. You can add flexibility to classes using **instance variables**. Their values are normally passed as arguments to `.__init__()` and stored as `self` attributes. For convenience, you can also provide reasonable default values.

To add `.text` as a `Timer` instance variable, you’ll do something like this:

```
def __init__(self, text="Elapsed time: {:0.4f} seconds"):
    self._start_time = None
    self.text = text
```

Note that the default text, `"Elapsed time: {:0.4f} seconds"`, is given as a regular string, not as an f-string. You can’t use an f-string here because they evaluate immediately, and when you instantiate `Timer`, your code has not yet calculated the elapsed time.

**Note:** If you want to use an f-string to specify `.text`, then you need to use double curly braces to escape the curly braces that the actual elapsed time will replace.

One example would be `f"Finished {task} in {{:0.4f}} seconds"`. If the value of `task` is `"reading"`, then this f-string would be evaluated as `"Finished reading in {:0.4f} seconds"`.

In `.stop()`, you use `.text` as a template and `.format()` to populate the template: