Start 
    XS var;
    var = 3 - 3 + 2;

    XS varTwo;

    rerun (var * 2 < 20) {
        var = var + 1;
        cond (var * 2 == 10) {
            varTwo = 50;
        }
    }
End