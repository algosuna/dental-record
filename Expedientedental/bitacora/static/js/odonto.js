        $(document).ready(function() {
            $('#color').dialog({
                autoOpen: false,
            });  
                $(".click").click(function(event) {
                var cuadro = $(this).find("input[name=cuadro]:hidden").val();//obtenemos el valor del cuadro al que le dimos click
                $( "#color" ).dialog( "option", "position", [event.pageX,event.pageY]);//posicionamos el elemento donde dimos click         
                $('#color').dialog('open');
                $(".select").click(function(event){
                    var color = $(this).css('background-color');
                    $("input[name=cuadro]:hidden").val(cuadro).parent(".cuadro").css('background-color', color);//establecemos el background a la clase cuadro
                });
                return false;
            });
                return false;           
        });