## Questions Asked
1. ```
      Write an implementation of the following interface for a key value store:
      
      void   put(key, val);
      V        get(key);
      void  delete(key);
      K       last();             // returns the last-accessed (put or get), non-deleted key
      K       random();    // returns a random key
      }
      
      Example:
      put("a", 1)
      last()                      => "a"
      last()                      => "a"
      
      put("b", 2)
      last()                      => "b"
      
      get("a")                 => 1
      last()                      => "a"
      
      delete("a")
      last()                      => "b"
   ```
2. Codebunk link
    1. https://codebunk.com/b/9811100710430/

### Feedback from IK portal

```
Topics Covered
HashTable, array, linked list
Problem Text
KV store with get/put/last/delete/random
Difficulty
Medium
Understanding
4 — The candidate quickly and clearly understood the problem, with little to no resistance in processing what was being asked.
Working Solution Proposed
3 — The candidate arrived at a working solution that sufficiently addressed problem requirements for a real-world interview.
Optimized Solution Proposed
3 — The solution was solidly interview-appropriate. It was both sufficiently performant and algorithmically/logically optimized.
Implementation
3 — The solution was implemented in code to a degree acceptable for a real-world interview.
Was a second problem attempted?
No
Brush-Up on Specific Topics
Coding speed seemed fine, but there were many cases missed, which can be a red flag in an interview. Keep that in mind when practicing coding
Verbal Explanation
3 — The candidate sufficiently explained their thinking around each solution.
Hints Needed
2 — The candidate relied on a fair amount of hinting, but also made not-insignificant progress on their own.
Hints Utilized
3 — The candidate listened to and responded sufficiently well to most hints.
Amount & Severity of Bugs
2 — The code was buggy, but not exceptionally buggy. That said, there were enough bugs that a red flag would be raised in a real-world interview.
Debugging
2 — The candidate could identify and fix some bugs on their own, but needed significant help from the interviewer. On the other hand, they struggled to fix important bugs or a sufficient amount of little bugs regardless of help.
Time & Space Complexity
3 — The candidate appears to sufficiently understand and communicate time and space complexity.
Code Readability
3 — The code was sufficiently readable.
Language Comfort
3 — The candidate seemed sufficiently comfortable with their programming language. Any quirks noticed are within the realm of acceptable. They are fluent enough to use this language in a real interview.
Communication
3 — Communication was strong. There may or may not have been a few minor quirks. Overall, it was sufficiently clear to pass a real-world interview.
Humility
4 — The candidate demonstrated exceptional humility. At no point could it even be possible to mistake this person as arrogant. It was a pleasure to engage with them.
Energy
3 — The candidate's energy was sufficient to high in one or more areas. Enthusiasm was expressed on a handful of topics and they give enough of an impression of embracing forward momentum.
Interview Anxiety
4 — No nervousness was detected at all. The candidate was very much at ease and/or highly confident.
Technical Score
2+ — Close, but not quite there yet. The candidate needs to improve in one or more areas to command definitive confidence from their interviewers.
Behavioral Score
3 — The candidate demonstrates strength across most behavioral criteria. Communication is strong, and they know how to listen and take hints. They ask good questions, may occasionally show enthusiasm, and generally has an overall good demeanor.
Hire Decision
No
Candidate Strengths
Good communication. I saw a lot of good points (coding speed seemed good, altho there were 4 bugs). Good listener, collaborative. Caught some of the hints very quickly. I can see the underlying concepts are clear, byt synthesizing those into a coherent solution for this problem took a bit of time initially. This problem is a good one to exercise that skill.
Additional Feedback
Let me know if any questions (my email is in the invite). KV store with get/put/last/delete/random: Good u looked thru the given example to get a good understanding. Should ask what time/space complexity is expected. Because for this, we want O(1) time for all interfaces. Had to give hints for linked list. Good job thinking that we can store the linked list node and index in the hash map. Good job realizing that deleting from an array would be linear time. For constant time deletion in an array, had to give a hint but u caught that quickly (that was good). Bugs ( 4 bugs ): Put: assumes the key is always new. Get, Put: Does tail need to get updated. Delete: index not updated for the key that was swapped from end. But when I told u there is a bug, u went thru code and found it.

```