
// For collapsible divs in Experiment Registration
$(document).ready(function() {
	$('.collapse').collapse();
	min_sensor_condition();
});

function validate_experiment(){
  var sCheckBoxes = $("#experiment .sensors");
  var sChecked = sCheckBoxes.filter(":checked");
  var error = "";
  if (sChecked.length === 0) {
      error += 'Atleast ONE sensor has to be selected\n';
//      return false;
  }
  else{
	for (i=0; i<sChecked.length; i++){
		var saCheckBoxes = $("#experiment .sensorattrs-"+sChecked[i].value);
		var saChecked = saCheckBoxes.filter(":checked");
		if(saChecked.length === 0) {
			error += 'Select atleast one checkbox under '+sChecked[i].getAttribute('data-label')+'\n';
//			return false;
		}
		else{
			for(j=0; j<saChecked.length; j++){
				var saLabelSuffix = sChecked[i].value+"-"+saChecked[j].value;
				if($("input[name=sensorattr_precision-"+saLabelSuffix+"]:checked").val() == 'truncate'){
					 if($("input[name=sensorattr_precision_value-"+saLabelSuffix+"]").val() == ''){
						error += 'Please fill in the truncation level you would prefer under '+saChecked[j].getAttribute('data-label')+'\n';
	                                }
				}
			}
		}
		if(document.getElementById("frequency-"+sChecked[i].value).value == ""){
			error += 'Please fill in frequency field under '+sChecked[i].getAttribute('data-label')+'\n';
		}
		if(document.getElementById("usage-"+sChecked[i].value).value == ""){
                        error += 'Please fill in usage field under '+sChecked[i].getAttribute('data-label')+'\n';
                }

	}
  }
	
	
//      for (var key in sChecked){
//	if (sChecked.hasOwnProperty(key)){
//		alert(sChecked[key].value);
//        }
//	else{
//		var obj = "NONE";
//        }
//      }
      //alert(obj +" "+ key);
  if(error!=""){
	alert(error);
	return false;
  }
  else{
	return true;
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
