$(function(){


	// target the input that counts the total forms
    var totalFormId = $("input[id='id_form-TOTAL_FORMS']");
    function getTotalForms(){
      return parseInt(totalFormId.val());
    }
    function setTotalForms(counter){
      totalFormId.attr('value', counter);
    }
    // Resta 1 por la forma que quita foreach.
    setTotalForms(getTotalForms()-1);

    // Isolates the number that should be incremented
    function updateElementIndex(elem, prefix, ndx) {
        var idRegex = new RegExp(prefix + '-(\\d+|__prefix__)-'),
            replacement = prefix + '-' + ndx + '-';
        if (elem.attr("for")) elem.attr("for", elem.attr("for").replace(idRegex, replacement));
        if (elem.attr('id')) elem.attr('id', elem.attr('id').replace(idRegex, replacement));
        if (elem.attr('name')) elem.attr('name', elem.attr('name').replace(idRegex, replacement));
    }

    function pushDataWrapper(vm, diente, cara, tratamiento, counter){
    	var form_div_id = "form_div_"+counter;

    	// Pushes the data with knockout and other things (part of odontograma.js)
    	vm.tratamientosAplicados.push({diente: diente, cara: cara, tratamiento: tratamiento, form_div_id: form_div_id});

    	// for each #form_div_1 update the index of the child div and its descendants
    	$('#'+form_div_id+' fieldset div').each(function(){
    		updateElementIndex($(this),'form',counter);
    		updateElementIndex($(this).children('label'),'form',counter);
    		updateElementIndex($(this).children('.controls').children(),'form',counter);
    	});
    }

})


