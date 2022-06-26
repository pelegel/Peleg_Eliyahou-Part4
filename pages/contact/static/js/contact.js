//ask the user to get promotion if didn't agree. if doesn't want promotions again - submiting the form
var times = 0;
var contact = 0;
function submitForm() {

  if (agree.checked == false && times ==0){
    window.alert("Are you sure you don't want to get promotion emails?");
    times+=1;
  }
  else if (times==1){
    window.alert("Thank you for contacting us!");
    times +=1;
    contact = 1;
  }
  else if (agree.checked == true && contact ==0){
    window.alert("Thank you for contacting us!");
    contact = 1;
  }
  else{
    window.alert("You have already submitted the form");
  }
}
