
// For collapsible divs in Experiment Registration
$(document).ready(function() {
	$('.collapse').collapse();
//	min_sensor_condition();
});

function min_sensor_condition(){
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
return error;	
}

function validate_email(){
	var email_fields = $('input[type="email"]');
	var err = "";
	if(email_fields.length != 0){
		var re = /^\s*[\w\-\+_]+(\.[\w\-\+_]+)*\@[\w\-\+_]+\.[\w\-\+_]+(\.[\w\-\+_]+)*\s*$/;

		for(i=0; i<email_fields.length; i++){
			var email = $('input[type="email"]')[i];
			if (!re.test(email.value)) {
				err += 'Not a valid e-mail address at "'+email.getAttribute('data-label')+'"\n';
			}
		}
	}

	return err;
}

function validate_experiment(){
	var error = "";
	error += min_sensor_condition();
	error += validate_email();
	
	if(error!=""){
		alert(error);
		return false;
	}
	else{
		return true;
	}

}
