
// For collapsible divs in Experiment Registration
$(document).ready(function() {
	$('#experiment .collapsible').change(function() {
		//$('#mycheckboxdiv').toggle();
		sensor_on_change(this.getAttribute('data-target'), this.checked);
	});
});

function sensor_on_change(target, flag){
    if(flag)
        $(target).show();
    else
        $(target).hide();
}

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
				if($("input[name="+saChecked[j].value+"-precision_choice]").val() == 'truncate'){
					 if($("input[name="+saChecked[j].value+"-precision_value]").val() == ''){
						error += 'Please fill in the truncation level you would prefer under '+saChecked[j].getAttribute('data-label')+'\n';
	                                }
				}
			}
		}
		if(document.getElementById("id_"+sChecked[i].value+"-frequency").value == ""){
			error += 'Please fill in frequency field under '+sChecked[i].getAttribute('data-label')+'\n';
		}
		if((document.getElementById("id_"+sChecked[i].value+"-downloadable-y").checked == false)
			&& (document.getElementById("id_"+sChecked[i].value+"-downloadable-n").checked == false)){
			error += 'Please answer if the selected sensor is Downloadable under '+sChecked[i].getAttribute('data-label')+'\n';
		}
		if(document.getElementById("id_"+sChecked[i].value+"-usage_policy").value == ""){
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
