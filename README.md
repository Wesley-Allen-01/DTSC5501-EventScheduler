# DTSC5501-EventScheduler

## Roles 

**Allen, Wesley:** Wesley was responsible for Part A, implementing an Array-based list and a Singly-linked list for storing events. He developed the overall structure for these lists and defined many basic operations for each. He also added placeholders for additional functions needed. Wesley helped the rest of the team refresh their GitHub skills and explained how to use Pytest. Wesley also implemented the experimentation and plotting for sorting in the main notebook.

**Cheemalapati, Karan:** Karan was responsible for Part D, focusing on scalability for handling up to 1 million events. He found that array-lists use about ~178 MB of memory compared to ~246 MB for linked lists, making them ~38% more efficient. He suggested improvements like indexing, hybrid structures, grouping events by date, and using databases. Karan also designed a parallel conflict detection method that splits events by date across CPU cores, and analyzed Big-O and performance results showing reduced time and memory use.

**Pulagalla, Srihari:** Srihari was responsible for Part B, implemented three sorting algorithms—Insertion Sort, Merge Sort, and Quick Sort—on both the ArrayList and LinkedList backends, sorting events by date and time and measured runtime for n = 50, 500, 5,000, and 50,000. Compared performance across both data structures, plotted the results.

**Teetsel, Amber:** Amber was responsible for Part C and Part E. She developed code for linear and binary searches including performance metrics (execution time, number of attempts). She also developed conflict-detection algorithms for array-based lists and for singly-linked lists. Amber assisted group members in getting started with GitHub and cleaned up the final notebook and .py files.
