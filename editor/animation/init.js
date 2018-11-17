//Dont change it
//Dont change it
requirejs(['ext_editor_io', 'jquery_190'],
    function (extIO, $) {
        var io = new extIO({
            multipleArguments: true,
            functions: {
                python: 'mult_two',
                js: 'multTwo'
            }
        });
        io.start();
    }
);
