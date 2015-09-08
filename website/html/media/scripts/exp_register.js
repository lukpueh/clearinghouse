
// For collapsible divs in Experiment Registration
$(document).ready(function() {
	$('.collapse').collapse();
	min_sensor_condition();
});

function validate_experiment(){
  var sCheckBoxes = $("#experiment .sensors");
  var sChecked = sCheckBoxes.filter(":checked");
  if (sChecked.length === 0) {
     // e.preventDefault();
      alert('Atleast ONE sensor has to be selected');
      return false;
  }
  else{
	for (i=0; i<sChecked.length; i++){
		var saCheckBoxes = $("#experiment .sensorattrs-"+sChecked[i].value);
		var saChecked = saCheckBoxes.filter(":checked");
		if(saChecked.length === 0) {
		alert('Select atleast one checkbox under '+sChecked[i].getAttribute('data-label'));
		return false;
		}
	}
	return false;
//      for (var key in sChecked){
//	if (sChecked.hasOwnProperty(key)){
//		alert(sChecked[key].value);
//        }
//	else{
//		var obj = "NONE";
//        }
//      }
      //alert(obj +" "+ key);
  }
}

function min_sensor_condition(){
	var checkedAtLeastOne = false;
	$('input[type="checkbox"][class="sensor"]').each(function() {
	    if ($(this).is(":checked")) {
	        checkedAtLeastOne = true;
	    }
	});
}
