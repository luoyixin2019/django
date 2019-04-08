
     var uploadfilename1;
     var a,b;
     var default_lng = 114.35,default_lat = 30.53;
     $(function(){
     //$( document.body ).ready( function(){
        var progressbar = $("#progressbar"),
            bar         = progressbar.find('.uk-progress-bar'),
            settings    = {
            single: false,
            filelimit: 1,

            action: '/uploadFile/', // upload url

            allow : '*.(jpg|png)', // allow war and zip

            loadstart: function() {
                bar.css("width", "0%").text("0%");
                progressbar.removeClass("uk-hidden");
            },

            progress: function(percent) {
                percent = Math.ceil(percent);
                bar.css("width", percent+"%").text(percent+"%");
            },

            allcomplete: function(response) {
                uploadfilename1 = response.replace(/\"/g,"")
                bar.css("width", "100%").text("100%");
                $("#upload-select").after("<div class='uk-alert' data-uk-alert> ���ϴ��ļ��� <span class='uk-text-success'>" + uploadfilename1 + "</span></div>");
                $("#file_path").attr("value", uploadfilename1);

                uploadfilename1_dir = 'images/' + uploadfilename1;

                ////////////
                 
                ///////////

                //use js to read the pic's width and height
                var img_url = 'static/images/' + uploadfilename1;
                var img = new Image();
                img.src = img_url;
                img.onload=function(){
                    console.log(img.width);
                a = default_lng + img.width*0.13/96000; //lng and lat of the pic covers
                b = default_lat + img.height*0.13/96000;                
                console.log(img.width);
                console.log(img.height);

                imageLayer1 = new AMap.ImageLayer({
                    url:'static/images/' + uploadfilename1,//done!
                bounds: new AMap.Bounds(
                    [default_lng,default_lat],
                    //[114.360809326,30.537185669]
                    [a,b]
                ),
                    zooms: [10, 22]
                });
                console.log(a);
                console.log(b);
                map.add(imageLayer1);////////////////////////////////////////////
                    
                    
                    
                };
                
                
                
                document.getElementById("open_pic").style.visibility="hidden";                

                //northEast=northEast.offset(a-default_lng,b-default_lat);
                
              
            }
        };
        var select = UIkit.uploadSelect($("#upload-select"), settings),
            drop   = UIkit.uploadDrop($("#upload-drop"), settings);
    });
