//calculate and print the average time the user listen to music according to it's input
function calcTime() {
  const numOfSongs = document.getElementById("inputNum").value;
  var res = "you listen to songs for an average time of ";
  res += numOfSongs*3.5;
  res += " minutes a day";
  document.getElementById("result").innerHTML = res;
}