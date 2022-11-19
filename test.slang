Start 
    XS var;
    var = 3 - 3 + 2;

     

    rerun (var * 2 < 20) {
        var = var + 1;
        rerun (var * 2 < 20) {
            var = var + 1;
        }
    }
End