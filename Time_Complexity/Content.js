let algo_array = [
    "Binary search","Linear search","Bubble sort","Insertion sort","Selection sort",
"Merge sort","Quick sort","Heap sort","Dijkstra's Algorithm","Kandane's Algorithm"
];
let time_array = [
    "O(logN)","O(N)","O(N^2)","O(N^2)","O(N^2)","O(NlogN)","O(N^2)","O(NlogN)","O(V^2)","O(N)"
];

function myfunction(arg)
{
    let x = Math.floor(Math.random()*algo_array.length());
    let s=document.getElementById("show");
    s.innerHTML("Time Complexity of " + algo_array[x] + " is " + time_array[x]);
}