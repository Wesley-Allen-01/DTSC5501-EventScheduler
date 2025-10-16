# DTSC5501-EventScheduler

## Roles 

**Allen, Wesley:** Wesley was responsible for Part A, implementing an Array-based list and a Singly-linked list for storing events. He developed the overall structure for these lists and defined many basic operations for each. He also added placeholders for additional functions needed. Wesley helped the rest of the team refresh their GitHub skills and explained how to use Pytest. Wesley also implemented the experimentation and plotting for sorting in the main notebook.

**Cheemalapati, Karan:** Karan was responsible for Part D, where he worked on the scalability part to handle up to 1 million events. He compared memory use and found that array-based lists need about ~178 MB, while linked lists need around ~246 MB i.e. 38% more efficient. He suggested improvements such as using indexes, combining data structures, grouping events by date for faster checks, and storing data in a database. Karan also outlined a parallel conflict detection design where events are split by date across multiple CPU cores to speed up the conflict detection process. His analysis also included Big-O comparisons and performance data showing how these methods reduce processing time and memory use.

**Pulagalla, Srihari:** Srihari was responsible for Part B, implemented three sorting algorithms—Insertion Sort, Merge Sort, and Quick Sort—on both the ArrayList and LinkedList backends, sorting events by date and time and measured runtime for n = 50, 500, 5,000, and 50,000. Compared performance across both data structures, plotted the results.

**Teetsel, Amber:** Amber was responsible for Part C and Part E. She developed code for linear and binary searches including performance metrics (execution time, number of attempts). She also developed conflict-detection algorithms for array-based lists and for singly-linked lists. Amber assisted group members in getting started with GitHub and cleaned up the final notebook and .py files.
