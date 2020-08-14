Template: article
Title: Java Garbage Collector Log 
Date: 2020-08-13
Slug: java-garbage-collector-log
Tags: java, garbage collector, log, datetime, python
Authors: kimyen


Have you ever read a Java garbage collector log? It's awful. It looks something like this:

```
...
[1930612.981s][info][safepoint     ] Entering safepoint region: Cleanup
[1930612.982s][info][safepoint     ] Leaving safepoint region
[1930612.982s][info][safepoint     ] Total time for which application threads were stopped: 0.0013979 seconds, Stopping threads took: 0.0003442 seconds
[1931020.084s][info][safepoint     ] Application time: 407.1018564 seconds
[1931020.085s][info][safepoint     ] Entering safepoint region: G1CollectForAllocation
[1931020.087s][info][gc,start      ] GC(20652) Pause Young (Normal) (G1 Evacuation Pause)
[1931020.087s][info][gc,task       ] GC(20652) Using 23 workers of 23 for evacuation
[1931020.236s][info][gc,phases     ] GC(20652)   Pre Evacuate Collection Set: 0.2ms
[1931020.236s][info][gc,phases     ] GC(20652)   Evacuate Collection Set: 135.4ms
[1931020.236s][info][gc,phases     ] GC(20652)   Post Evacuate Collection Set: 10.5ms
[1931020.236s][info][gc,phases     ] GC(20652)   Other: 3.2ms
[1931020.236s][info][gc,heap       ] GC(20652) Eden regions: 3388->0(3316)
[1931020.236s][info][gc,heap       ] GC(20652) Survivor regions: 35->41(428)
[1931020.236s][info][gc,heap       ] GC(20652) Old regions: 1221->1221
[1931020.236s][info][gc,heap       ] GC(20652) Humongous regions: 10->2
[1931020.236s][info][gc,metaspace  ] GC(20652) Metaspace: 347213K->347213K(475136K)
[1931020.236s][info][gc            ] GC(20652) Pause Young (Normal) (G1 Evacuation Pause) 148885M->40435M(196608M) 149.357ms
[1931020.236s][info][gc,cpu        ] GC(20652) User=3.24s Sys=0.00s Real=0.15s
...
```

Imagine you are looking for the root cause of an application crash and trying to get a picture of what is going on with different part of the system. One important part of a java application is the garbage collector. Say that you want to figure out, at 16:50 to 17:15 on 2020-07-24, how was the garbage collector doing? Good luck finding that information using the log above where the time is in seconds!

Luckily, the name of the garbage collector log file contains the time at which the application starts. And the time (in seconds) within the log is the second since the application starts. Based on that, I wrote a [tiny python script](https://github.com/kimyen/gc_date_format) that takes the original garbage collector log and output one with ISO datetime format. Something like this would be much easier to navigate:

```
...
2020-07-24T16:15:06.514000[1931961.514s][info][safepoint     ] Total time for which application threads were stopped: 0.0012066 seconds, Stopping threads took: 0.0003581 seconds
2020-07-24T16:24:01.020000[1932496.020s][info][safepoint     ] Application time: 534.5060495 seconds
2020-07-24T16:24:01.021000[1932496.021s][info][safepoint     ] Entering safepoint region: G1CollectForAllocation
2020-07-24T16:24:01.024000[1932496.024s][info][gc,start      ] GC(20654) Pause Young (Normal) (G1 Evacuation Pause)
2020-07-24T16:24:01.024000[1932496.024s][info][gc,task       ] GC(20654) Using 23 workers of 23 for evacuation
2020-07-24T16:24:01.099000[1932496.099s][info][gc,phases     ] GC(20654)   Pre Evacuate Collection Set: 0.2ms
2020-07-24T16:24:01.099000[1932496.099s][info][gc,phases     ] GC(20654)   Evacuate Collection Set: 61.0ms
2020-07-24T16:24:01.099000[1932496.099s][info][gc,phases     ] GC(20654)   Post Evacuate Collection Set: 10.6ms
2020-07-24T16:24:01.099000[1932496.099s][info][gc,phases     ] GC(20654)   Other: 3.2ms
2020-07-24T16:24:01.099000[1932496.099s][info][gc,heap       ] GC(20654) Eden regions: 3364->0(3670)
2020-07-24T16:24:01.099000[1932496.099s][info][gc,heap       ] GC(20654) Survivor regions: 37->16(426)
2020-07-24T16:24:01.099000[1932496.099s][info][gc,heap       ] GC(20654) Old regions: 1221->1222
2020-07-24T16:24:01.099000[1932496.099s][info][gc,heap       ] GC(20654) Humongous regions: 2->2
2020-07-24T16:24:01.099000[1932496.099s][info][gc,metaspace  ] GC(20654) Metaspace: 347628K->347628K(475136K)
2020-07-24T16:24:01.099000[1932496.099s][info][gc            ] GC(20654) Pause Young (Normal) (G1 Evacuation Pause) 147937M->39650M(196608M) 75.105ms
2020-07-24T16:24:01.099000[1932496.099s][info][gc,cpu        ] GC(20654) User=1.23s Sys=0.28s Real=0.07s
2020-07-24T16:24:01.099000[1932496.099s][info][safepoint     ] Leaving safepoint region
2020-07-24T16:24:01.099000[1932496.099s][info][safepoint     ] Total time for which application threads were stopped: 0.0792423 seconds, Stopping threads took: 0.0004899 seconds
2020-07-24T16:24:05.541000[1932500.541s][info][safepoint     ] Application time: 4.4411200 seconds
2020-07-24T16:24:05.541000[1932500.541s][info][safepoint     ] Entering safepoint region: ThreadDump
...
```

Well, if you are reading GC log, good luck! ;)

