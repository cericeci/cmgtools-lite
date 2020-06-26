#include <iostream>

// the final bit: 58 bins
int SRcorr(float mll, float mT, float met, float ht, int offset = 0) {

    if(              mll <  75 && ht >=  0 && ht < 200) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset +  1;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset +  2;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset +  3;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset +  4;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset +  5;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset +  6;
        if(mT >= 100 && mT < 160 && met >= 150             ) return offset +  7;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset +  8;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset +  9;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 10;
        if(mT >= 160 &&             met >= 200             ) return offset + 11;
    }
    if(              mll <  75 && ht >= 200            ) {
        if(mT >=   0 && mT < 100                           ) return offset + 12;
        if(mT >= 100 && mT < 160                           ) return offset + 13;
        if(mT >= 160                                       ) return offset + 14;
    }
    if(mll >=  75 && mll < 105 && ht >=  0 && ht < 100) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return 0          ; // this is the WZ CR !
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 15;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 16;
        if(mT >=   0 && mT < 100 && met >= 200 && met < 250) return offset + 17;
        if(mT >=   0 && mT < 100 && met >= 250             ) return offset + 18;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 19;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 20;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 21;
        if(mT >= 100 && mT < 160 && met >= 200             ) return offset + 22;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 23;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 24;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 25;
        if(mT >= 160 &&             met >= 200             ) return offset + 26;
    }
    if(mll >=  75 && mll < 105 && ht >= 100 && ht < 200) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 27;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 28;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 29;
        if(mT >=   0 && mT < 100 && met >= 200 && met < 250) return offset + 30;
        if(mT >=   0 && mT < 100 && met >= 250             ) return offset + 31;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 32;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 33;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 34;
        if(mT >= 100 && mT < 160 && met >= 200             ) return offset + 35;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 36;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 37;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 38;
        if(mT >= 160 &&             met >= 200             ) return offset + 39;
    }
    if(mll >=  75 && mll < 105 && ht >= 200            ) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 150) return offset + 40;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 250) return offset + 41;
        if(mT >=   0 && mT < 100 && met >= 250 && met < 350) return offset + 42;
        if(mT >=   0 && mT < 100 && met >= 350             ) return offset + 43;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 44;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 45;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 46;
        if(mT >= 100 && mT < 160 && met >= 200 && met < 250) return offset + 47;
        if(mT >= 100 && mT < 160 && met >= 250 && met < 300) return offset + 48;
        if(mT >= 100 && mT < 160 && met >= 300             ) return offset + 49;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 50;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 51;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 52;
        if(mT >= 160 &&             met >= 200 && met < 250) return offset + 53;
        if(mT >= 160 &&             met >= 250 && met < 300) return offset + 54;
        if(mT >= 160 &&             met >= 300             ) return offset + 55;
    }
    if(mll >= 105                                      ) {
        if(mT >=   0 && mT < 100                           ) return offset + 56;
        if(mT >= 100 && mT < 160                           ) return offset + 57;
        if(mT >= 160                                       ) return offset + 58;
    } 
    return 0;
}



// optimization stuff below
// =============================================================================
// =============================================================================

int SRwz(float mT2L, float mT2T, float mll, float mT, float met, int offset = 0) {

    if(mll >= 75 && mll < 105) {
        if (mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 15;
        if (mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 16;
        if (mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 17;
        if (mT >=   0 && mT < 100 && met >= 200 && met < 250) return offset + 18;
        if (mT >=   0 && mT < 100 && met >= 250 && met < 400) return offset + 19;
        if (mT >=   0 && mT < 100 && met >= 400 && met < 550) return offset + 20;
        if (mT >=   0 && mT < 100 && met >= 550             ) return offset + 21;
        if (mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 22;
        if (mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 23;
        if (mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 24;
        if (mT >= 100 && mT < 160 && met >= 200             ) return offset + 25;
        if (mT >= 160 &&             met >=   0 && met < 100) return offset + 26;
        if (mT >= 160 &&             met >= 100 && met < 150) return offset + 27;
        if (mT >= 160 &&             met >= 150 && met < 200) return offset + 28;
        if (mT >= 160 &&             met >= 200 && met < 250) return offset + 29;
        if (mT >= 160 &&             met >= 250 && met < 400) return offset + 30;
        if (mT >= 160 &&             met >= 400             ) return offset + 31;
    }
    return 0;
}


int SRwzMll(float mll, float mT, float met, int offset = 0) {

    if(mll >= 0 && mll < 75) {
        if (mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset +  1;
        if (mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset +  2;
        if (mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset +  3;
        if (mT >=   0 && mT < 100 && met >= 200             ) return offset +  4;
        if (mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset +  5;
        if (mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset +  6;
        if (mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset +  7;
        if (mT >= 100 && mT < 160 && met >= 200             ) return offset +  8;
        if (mT >= 160 &&             met >=   0 && met < 100) return offset +  9;
        if (mT >= 160 &&             met >= 100 && met < 150) return offset + 10;
        if (mT >= 160 &&             met >= 150 && met < 200) return offset + 11;
        if (mT >= 160 &&             met >= 200             ) return offset + 12;
    }
    if(mll >= 75 && mll < 105) {
        if (mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 13;
        if (mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 14;
        if (mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 15;
        if (mT >=   0 && mT < 100 && met >= 200             ) return offset + 16;
        if (mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 17;
        if (mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 18;
        if (mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 19;
        if (mT >= 100 && mT < 160 && met >= 200             ) return offset + 20;
        if (mT >= 160 &&             met >=   0 && met < 100) return offset + 21;
        if (mT >= 160 &&             met >= 100 && met < 150) return offset + 22;
        if (mT >= 160 &&             met >= 150 && met < 200) return offset + 23;
        if (mT >= 160 &&             met >= 200             ) return offset + 24;
    }
    if(mll >= 105) {
        if (mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 25;
        if (mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 26;
        if (mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 27;
        if (mT >=   0 && mT < 100 && met >= 200             ) return offset + 28;
        if (mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 29;
        if (mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 30;
        if (mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 31;
        if (mT >= 100 && mT < 160 && met >= 200             ) return offset + 32;
        if (mT >= 160 &&             met >=   0 && met < 100) return offset + 33;
        if (mT >= 160 &&             met >= 100 && met < 150) return offset + 34;
        if (mT >= 160 &&             met >= 150 && met < 200) return offset + 35;
        if (mT >= 160 &&             met >= 200             ) return offset + 36;
    }
    return 0;
}

int SRwz2(float lep1pt, float mT2L, float mT2T, float mll, float mT, float met, int offset = 0) {
    if(lep1pt < 200) 
        return SRwzMll(mll, mT, met, 0);
    else
        return SRwzMll(mll, mT, met, 36);
}

int SRwz3fine(float mll, float mT, float met, float ht, int offset = 0) {
    if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset +  1;
    if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset +  2;
    if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset +  3;
    if(mT >=   0 && mT < 100 && met >= 200             ) return offset +  4;
    if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset +  5;
    if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset +  6;
    if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset +  7;
    if(mT >= 100 && mT < 160 && met >= 200             ) return offset +  8;
    if(mT >= 160 &&             met >=   0 && met < 100) return offset +  9;
    if(mT >= 160 &&             met >= 100 && met < 150) return offset + 10;
    if(mT >= 160 &&             met >= 150 && met < 200) return offset + 11;
    if(mT >= 160 &&             met >= 200             ) return offset + 12;
    return 0;
}

int SRwz3finer(float mll, float mT, float met, float ht, int offset = 0) {
    if(mT >=   0 && mT <  40 && met >=   0 && met < 100) return offset +  1;
    if(mT >=   0 && mT <  40 && met >= 100 && met < 150) return offset +  2;
    if(mT >=   0 && mT <  40 && met >= 150 && met < 200) return offset +  3;
    if(mT >=   0 && mT <  40 && met >= 200             ) return offset +  4;
    if(mT >=  40 && mT < 100 && met >=   0 && met < 100) return offset +  5;
    if(mT >=  40 && mT < 100 && met >= 100 && met < 150) return offset +  6;
    if(mT >=  40 && mT < 100 && met >= 150 && met < 200) return offset +  7;
    if(mT >=  40 && mT < 100 && met >= 200             ) return offset +  8;
    if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset +  9;
    if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 10;
    if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 11;
    if(mT >= 100 && mT < 160 && met >= 200             ) return offset + 12;
    if(mT >= 160 &&             met >=   0 && met < 100) return offset + 13;
    if(mT >= 160 &&             met >= 100 && met < 150) return offset + 14;
    if(mT >= 160 &&             met >= 150 && met < 200) return offset + 15;
    if(mT >= 160 &&             met >= 200             ) return offset + 16;
    return 0;
}


int SRwz3(float mll, float mT, float met, float ht, int offset = 0) {

    if(ht >=   0 && ht <  50) return SRwz3finer(mll, mT, met, ht,  0);
    if(ht >=  50 && ht < 150) return SRwz3finer(mll, mT, met, ht, 16);
    if(ht >= 150 && ht < 300) return SRwz3finer(mll, mT, met, ht, 32);
    if(ht >= 300            ) return SRwz3finer(mll, mT, met, ht, 48);
    return 0;
}

int SRwz4(float mll, float mT, float met, float ht, int offset = 0) {

    if(              mll <  75 && ht >=   0 && ht < 100) return SRwz3fine(mll, mT, met, ht,  0);
    if(              mll <  75 && ht >= 100 && ht < 200) return SRwz3fine(mll, mT, met, ht, 12);
    if(              mll <  75 && ht >= 200            ) return SRwz3fine(mll, mT, met, ht, 24);
    if(mll >=  75 && mll < 105 && ht >=   0 && ht < 100) return SRwz3fine(mll, mT, met, ht, 36);
    if(mll >=  75 && mll < 105 && ht >= 100 && ht < 200) return SRwz3fine(mll, mT, met, ht, 48);
    if(mll >=  75 && mll < 105 && ht >= 200            ) return SRwz3fine(mll, mT, met, ht, 60);
    if(mll >= 105              && ht >=   0 && ht < 100) return SRwz3fine(mll, mT, met, ht, 72);
    if(mll >= 105              && ht >= 100 && ht < 200) return SRwz3fine(mll, mT, met, ht, 84);
    if(mll >= 105              && ht >= 200            ) return SRwz3fine(mll, mT, met, ht, 96);
    return 0;
}

int SRwz4p1(float mll, float mT, float met, float ht, int offset = 0) {

    if(              mll <  75 && ht >=   0 && ht < 100) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset +  1;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset +  2;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset +  3;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset +  4;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset +  5;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset +  6;
        if(mT >= 100 && mT < 160 && met >= 150             ) return offset +  7;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset +  8;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset +  9;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 10;
        if(mT >= 160 &&             met >= 200             ) return offset + 11;
    }
    if(              mll <  75 && ht >= 100 && ht < 200) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 12;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 13;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 14;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset + 15;
        if(mT >= 100 &&             met >=   0 && met < 100) return offset + 16;
        if(mT >= 100 &&             met >= 100 && met < 150) return offset + 17;
        if(mT >= 100 &&             met >= 150             ) return offset + 18;
    }
    if(              mll <  75 && ht >= 200            ) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 19;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 20;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 21;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset + 22;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 23;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 24;
        if(mT >= 100 && mT < 160 && met >= 150             ) return offset + 25;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 26;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 27;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 28;
        if(mT >= 160 &&             met >= 200             ) return offset + 29;
    }
    if(mll >=  75 && mll < 105 && ht >=   0 && ht < 100) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 30;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 31;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 32;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset + 33;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 34;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 35;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 36;
        if(mT >= 100 && mT < 160 && met >= 200             ) return offset + 37;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 38;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 39;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 40;
        if(mT >= 160 &&             met >= 200             ) return offset + 41;
    }
    if(mll >=  75 && mll < 105 && ht >= 100 && ht < 200) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 42;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 43;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 44;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset + 45;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 46;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 47;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 48;
        if(mT >= 100 && mT < 160 && met >= 200             ) return offset + 49;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 50;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 51;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 52;
        if(mT >= 160 &&             met >= 200             ) return offset + 53;
    }
    if(mll >=  75 && mll < 105 && ht >= 200            ) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 54;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 55;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 56;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset + 57;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 58;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 59;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 60;
        if(mT >= 100 && mT < 160 && met >= 200             ) return offset + 61;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 62;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 63;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 64;
        if(mT >= 160 &&             met >= 200             ) return offset + 65;
    }
    if(mll >= 105              && ht >=   0 && ht < 100) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 66;
        if(mT >=   0 && mT < 100 && met >= 100             ) return offset + 67;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 68;
        if(mT >= 100 && mT < 160 && met >= 100             ) return offset + 69;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 70;
        if(mT >= 160 &&             met >= 100             ) return offset + 71;
    } 
    if(mll >= 105              && ht >= 100 && ht < 200) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 72;
        if(mT >=   0 && mT < 100 && met >= 100             ) return offset + 73;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 74;
        if(mT >= 100 && mT < 160 && met >= 100             ) return offset + 75;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 76;
        if(mT >= 160 &&             met >= 100             ) return offset + 77;
    } 
    if(mll >= 105              && ht >= 200            ) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 78;
        if(mT >=   0 && mT < 100 && met >= 100             ) return offset + 79;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 80;
        if(mT >= 100 && mT < 160 && met >= 100             ) return offset + 81;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 82;
        if(mT >= 160 &&             met >= 100             ) return offset + 83;
    } 
    return 0;
}

int SRwz4p2(float mll, float mT, float met, float ht, int offset = 0) {

    if(              mll <  75 && ht >=   0 && ht < 100) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset +  1;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset +  2;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset +  3;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset +  4;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset +  5;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset +  6;
        if(mT >= 100 && mT < 160 && met >= 150             ) return offset +  7;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset +  8;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset +  9;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 10;
        if(mT >= 160 &&             met >= 200             ) return offset + 11;
    }
    if(              mll <  75 && ht >= 100 && ht < 200) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 12;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 13;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 14;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset + 15;
        if(mT >= 100 &&             met >=   0 && met < 100) return offset + 16;
        if(mT >= 100 &&             met >= 100 && met < 150) return offset + 17;
        if(mT >= 100 &&             met >= 150             ) return offset + 18;
    }
    if(              mll <  75 && ht >= 200            ) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 19;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 20;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 21;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset + 22;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 23;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 24;
        if(mT >= 100 && mT < 160 && met >= 150             ) return offset + 25;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 26;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 27;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 28;
        if(mT >= 160 &&             met >= 200             ) return offset + 29;
    }
    if(mll >=  75 && mll < 105 && ht >=   0 && ht < 100) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 30;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 31;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 32;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset + 33;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 34;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 35;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 36;
        if(mT >= 100 && mT < 160 && met >= 200             ) return offset + 37;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 38;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 39;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 40;
        if(mT >= 160 &&             met >= 200             ) return offset + 41;
    }
    if(mll >=  75 && mll < 105 && ht >= 100 && ht < 200) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 42;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 43;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 44;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset + 45;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 46;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 47;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 48;
        if(mT >= 100 && mT < 160 && met >= 200             ) return offset + 49;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 50;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 51;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 52;
        if(mT >= 160 &&             met >= 200             ) return offset + 53;
    }
    if(mll >=  75 && mll < 105 && ht >= 200            ) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 54;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 55;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 56;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset + 57;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 58;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 59;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 60;
        if(mT >= 100 && mT < 160 && met >= 200             ) return offset + 61;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 62;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 63;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 64;
        if(mT >= 160 &&             met >= 200             ) return offset + 65;
    }
    if(mll >= 105                                      ) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 66;
        if(mT >=   0 && mT < 100 && met >= 100             ) return offset + 67;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 68;
        if(mT >= 100 && mT < 160 && met >= 100             ) return offset + 69;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 70;
        if(mT >= 160 &&             met >= 100             ) return offset + 71;
    } 
    return 0;
}

int SRwz4p3(float mll, float mT, float met, float ht, int offset = 0) {

    if(              mll <  75 && ht >=  30 && ht < 200) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset +  1;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset +  2;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset +  3;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset +  4;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset +  5;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset +  6;
        if(mT >= 100 && mT < 160 && met >= 150             ) return offset +  7;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset +  8;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset +  9;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 10;
        if(mT >= 160 &&             met >= 200             ) return offset + 11;
    }
    if(              mll <  75 && ht >= 200            ) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 12;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 13;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 14;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset + 15;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 16;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 17;
        if(mT >= 100 && mT < 160 && met >= 150             ) return offset + 18;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 19;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 20;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 21;
        if(mT >= 160 &&             met >= 200             ) return offset + 22;
    }
    if(mll >=  75 && mll < 105 && ht >=  30 && ht < 100) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 23;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 24;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 25;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset + 26;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 27;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 28;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 29;
        if(mT >= 100 && mT < 160 && met >= 200             ) return offset + 30;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 31;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 32;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 33;
        if(mT >= 160 &&             met >= 200             ) return offset + 34;
    }
    if(mll >=  75 && mll < 105 && ht >= 100 && ht < 200) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 35;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 36;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 37;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset + 38;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 39;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 40;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 41;
        if(mT >= 100 && mT < 160 && met >= 200             ) return offset + 42;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 43;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 44;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 45;
        if(mT >= 160 &&             met >= 200             ) return offset + 46;
    }
    if(mll >=  75 && mll < 105 && ht >= 200            ) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 47;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 48;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 49;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset + 50;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 51;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 52;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 53;
        if(mT >= 100 && mT < 160 && met >= 200             ) return offset + 54;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 55;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 56;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 57;
        if(mT >= 160 &&             met >= 200             ) return offset + 58;
    }
    if(mll >= 105                                      ) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 59;
        if(mT >=   0 && mT < 100 && met >= 100             ) return offset + 60;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 61;
        if(mT >= 100 && mT < 160 && met >= 100             ) return offset + 62;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 63;
        if(mT >= 160 &&             met >= 100             ) return offset + 64;
    } 
    return 0;
}

int SRwz4p4(float mll, float mT, float met, float ht, int offset = 0) {

    if(              mll <  75 && ht >=  0 && ht < 200) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset +  1;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset +  2;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset +  3;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset +  4;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset +  5;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset +  6;
        if(mT >= 100 && mT < 160 && met >= 150             ) return offset +  7;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset +  8;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset +  9;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 10;
        if(mT >= 160 &&             met >= 200             ) return offset + 11;
    }
    if(              mll <  75 && ht >= 200            ) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 12;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 13;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 14;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset + 15;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 16;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 17;
        if(mT >= 100 && mT < 160 && met >= 150             ) return offset + 18;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 19;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 20;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 21;
        if(mT >= 160 &&             met >= 200             ) return offset + 22;
    }
    if(mll >=  75 && mll < 105 && ht >=  0 && ht < 100) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 23;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 24;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 25;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset + 26;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 27;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 28;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 29;
        if(mT >= 100 && mT < 160 && met >= 200             ) return offset + 30;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 31;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 32;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 33;
        if(mT >= 160 &&             met >= 200             ) return offset + 34;
    }
    if(mll >=  75 && mll < 105 && ht >= 100 && ht < 200) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 35;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 36;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 37;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset + 38;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 39;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 40;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 41;
        if(mT >= 100 && mT < 160 && met >= 200             ) return offset + 42;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 43;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 44;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 45;
        if(mT >= 160 &&             met >= 200             ) return offset + 46;
    }
    if(mll >=  75 && mll < 105 && ht >= 200            ) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 47;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 48;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 49;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset + 50;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 51;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 52;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 53;
        if(mT >= 100 && mT < 160 && met >= 200             ) return offset + 54;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 55;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 56;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 57;
        if(mT >= 160 &&             met >= 200             ) return offset + 58;
    }
    if(mll >= 105                                      ) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 59;
        if(mT >=   0 && mT < 100 && met >= 100             ) return offset + 60;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 61;
        if(mT >= 100 && mT < 160 && met >= 100             ) return offset + 62;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 63;
        if(mT >= 160 &&             met >= 100             ) return offset + 64;
    } 
    return 0;
}

int SRwz4p5(float mll, float mT, float met, float ht, int offset = 0) {

    if(              mll <  75 && ht >=  0 && ht < 200) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset +  1;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset +  2;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset +  3;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset +  4;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset +  5;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset +  6;
        if(mT >= 100 && mT < 160 && met >= 150             ) return offset +  7;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset +  8;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset +  9;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 10;
        if(mT >= 160 &&             met >= 200             ) return offset + 11;
    }
    if(              mll <  75 && ht >= 200            ) {
        if(mT >=   0 && mT < 100                           ) return offset + 12;
        if(mT >= 100 && mT < 160                           ) return offset + 13;
        if(mT >= 160                                       ) return offset + 14;
    }
    if(mll >=  75 && mll < 105 && ht >=  0 && ht < 100) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 15;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 16;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 17;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset + 18;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 19;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 20;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 21;
        if(mT >= 100 && mT < 160 && met >= 200             ) return offset + 22;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 23;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 24;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 25;
        if(mT >= 160 &&             met >= 200             ) return offset + 26;
    }
    if(mll >=  75 && mll < 105 && ht >= 100 && ht < 200) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 27;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 28;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 29;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset + 30;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 31;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 32;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 33;
        if(mT >= 100 && mT < 160 && met >= 200             ) return offset + 34;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 35;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 36;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 37;
        if(mT >= 160 &&             met >= 200             ) return offset + 38;
    }
    if(mll >=  75 && mll < 105 && ht >= 200            ) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 39;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 40;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 41;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset + 42;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 43;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 44;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 45;
        if(mT >= 100 && mT < 160 && met >= 200             ) return offset + 46;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 47;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 48;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 49;
        if(mT >= 160 &&             met >= 200             ) return offset + 50;
    }
    if(mll >= 105                                      ) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 51;
        if(mT >=   0 && mT < 100 && met >= 100             ) return offset + 52;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 53;
        if(mT >= 100 && mT < 160 && met >= 100             ) return offset + 54;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 55;
        if(mT >= 160 &&             met >= 100             ) return offset + 56;
    } 
    return 0;
}

int SRwz4p6(float mll, float mT, float met, float ht, int offset = 0) {

    if(              mll <  75 && ht >=  0 && ht < 200) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset +  1;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset +  2;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset +  3;
        if(mT >=   0 && mT < 100 && met >= 200             ) return offset +  4;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset +  5;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset +  6;
        if(mT >= 100 && mT < 160 && met >= 150             ) return offset +  7;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset +  8;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset +  9;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 10;
        if(mT >= 160 &&             met >= 200             ) return offset + 11;
    }
    if(              mll <  75 && ht >= 200            ) {
        if(mT >=   0 && mT < 100                           ) return offset + 12;
        if(mT >= 100 && mT < 160                           ) return offset + 13;
        if(mT >= 160                                       ) return offset + 14;
    }
    if(mll >=  75 && mll < 105 && ht >=  0 && ht < 100) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 15;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 16;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 17;
        if(mT >=   0 && mT < 100 && met >= 200 && met < 250) return offset + 18;
        if(mT >=   0 && mT < 100 && met >= 300             ) return offset + 19;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 20;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 21;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 22;
        if(mT >= 100 && mT < 160 && met >= 200             ) return offset + 23;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 24;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 25;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 26;
        if(mT >= 160 &&             met >= 200             ) return offset + 27;
    }
    if(mll >=  75 && mll < 105 && ht >= 100 && ht < 200) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 28;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 29;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 30;
        if(mT >=   0 && mT < 100 && met >= 200 && met < 250) return offset + 31;
        if(mT >=   0 && mT < 100 && met >= 250             ) return offset + 32;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 33;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 34;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 35;
        if(mT >= 100 && mT < 160 && met >= 200             ) return offset + 36;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 37;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 38;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 39;
        if(mT >= 160 &&             met >= 200             ) return offset + 40;
    }
    if(mll >=  75 && mll < 105 && ht >= 200            ) {
        if(mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 41;
        if(mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 42;
        if(mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 43;
        if(mT >=   0 && mT < 100 && met >= 200 && met < 250) return offset + 44;
        if(mT >=   0 && mT < 100 && met >= 250 && met < 300) return offset + 45;
        if(mT >=   0 && mT < 100 && met >= 300 && met < 350) return offset + 46;
        if(mT >=   0 && mT < 100 && met >= 350             ) return offset + 47;
        if(mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 48;
        if(mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 49;
        if(mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 50;
        if(mT >= 100 && mT < 160 && met >= 200 && met < 250) return offset + 51;
        if(mT >= 100 && mT < 160 && met >= 250 && met < 300) return offset + 52;
        if(mT >= 100 && mT < 160 && met >= 300             ) return offset + 53;
        if(mT >= 160 &&             met >=   0 && met < 100) return offset + 54;
        if(mT >= 160 &&             met >= 100 && met < 150) return offset + 55;
        if(mT >= 160 &&             met >= 150 && met < 200) return offset + 56;
        if(mT >= 160 &&             met >= 200 && met < 250) return offset + 57;
        if(mT >= 160 &&             met >= 250 && met < 300) return offset + 58;
        if(mT >= 160 &&             met >= 300             ) return offset + 59;
    }
    if(mll >= 105                                      ) {
        if(mT >=   0 && mT < 100                           ) return offset + 60;
        if(mT >= 100 && mT < 160                           ) return offset + 61;
        if(mT >= 160                                       ) return offset + 62;
    } 
    return 0;
}


// SSR
// =============================================================================
// =============================================================================

int SuperSigcorr1(float mll, float mT, float met, float ht, int offset = 0) {
    if(mT>100 && met>200 && ht>200) return 1;
    return 0;
}
int SuperSigcorr2(float mll, float mT, float met, float ht, int offset = 0) {
    if(mT>100 && met>200) return 1;
    return 0;
}
int SuperSigcorr3(float mll, float mT, float met, float ht, int offset = 0) {
    if(met>200) return 1;
    return 0;
}
int SuperSigcorr4(float mll, float mT, float met, float ht, int offset = 0) {
    if(mll>86 && mll<96 && met>200) return 1;
    return 0;
}
int SuperSigcorr5(float mll, float mT, float met, float ht, int offset = 0) {
    if(mll>86 && mll<96 && met>300 && ht>200) return 1;
    return 0;
}
int SuperSigcorr6(float mll, float mT, float met, float ht, int offset = 0) {
    if(mll>86 && mll<96 && met>300) return 1;
    return 0;
}

int CountNJNBJ(int nJ, int nBJ){
    if (nBJ >= 2) nBJ = 2;
    nJ = nJ - nBJ;
    if (nJ >=  4) nJ = 4;
    return 5*nBJ+ nJ;
}



Float_t wzweight16(Float_t met, Float_t mt,Float_t side){
    Float_t var;
    if (met < 100){
        if (mt < 100) var = 0.06;
        else if (mt < 160) var = 0.07;
        else var = 0.13;
    }
    else if (met < 200){
        if (mt < 100) var = 0.07;
        else if (mt < 160) var = 0.10;
        else var = 0.15;
    }
    else {
        if (mt < 100) var = 0.14;
        else if (mt < 160) var = 0.29;
        else var = 0.20;
    }
    return 1 + var*side;
}


Float_t wzweight17(Float_t met, Float_t mt,Float_t side){
    Float_t var;
    if (met < 100){
        if (mt < 100) var = 0.09;
        else if (mt < 160) var = 0.07;
        else var = 0.09;
    }
    else if (met < 200){
        if (mt < 100) var = 0.08;
        else if (mt < 160) var = 0.13;
        else var = 0.11;
    }
    else {
        if (mt < 100) var = 0.10;
        else if (mt < 160) var = 0.19;
        else var = 0.16;
    }
    return 1 + var*side;
}


Float_t wzweight18(Float_t met, Float_t mt,Float_t side){
    Float_t var;
    if (met < 100){
        if (mt < 100) var = 0.09;
        else if (mt < 160) var = 0.10;
        else var = 0.11;
    }
    else if (met < 200){
        if (mt < 100) var = 0.07;
        else if (mt < 160) var = 0.09;
        else var = 0.10;
    }
    else {
        if (mt < 100) var = 0.11;
        else if (mt < 160) var = 0.21;
        else var = 0.15;
    }
    return 1 + var*side;
}
//SRs

int SR3lA(float mT2L, float mT2T, float mll, float mT, float met, int offset = 0) {

    if(mll >= 0 && mll < 75) {
        if (mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset +  1;
        if (mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset +  2;
        if (mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset +  3;
        if (mT >=   0 && mT < 100 && met >= 200 && met < 250) return offset +  4;
        if (mT >=   0 && mT < 100 && met >= 250             ) return offset +  5;
        if (mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset +  6;
        if (mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset +  7;
        if (mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset +  8;
        if (mT >= 100 && mT < 160 && met >= 200             ) return offset +  9;
        if (mT >= 160 &&             met >=   0 && met < 100) return offset + 10;
        if (mT >= 160 &&             met >= 100 && met < 150) return offset + 11;
        if (mT >= 160 &&             met >= 150 && met < 200) return offset + 12;
        if (mT >= 160 &&             met >= 200 && met < 250) return offset + 13;
        if (mT >= 160 &&             met >= 250             ) return offset + 14;
    }
    if(mll >= 75 && mll < 105) {
        if (mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 15;
        if (mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 16;
        if (mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 17;
        if (mT >=   0 && mT < 100 && met >= 200 && met < 250) return offset + 18;
        if (mT >=   0 && mT < 100 && met >= 250 && met < 400) return offset + 19;
        if (mT >=   0 && mT < 100 && met >= 400 && met < 550) return offset + 20;
        if (mT >=   0 && mT < 100 && met >= 550             ) return offset + 21;
        if (mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 22;
        if (mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 23;
        if (mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 24;
        if (mT >= 100 && mT < 160 && met >= 200             ) return offset + 25;
        if (mT >= 160 &&             met >=   0 && met < 100) return offset + 26;
        if (mT >= 160 &&             met >= 100 && met < 150) return offset + 27;
        if (mT >= 160 &&             met >= 150 && met < 200) return offset + 28;
        if (mT >= 160 &&             met >= 200 && met < 250) return offset + 29;
        if (mT >= 160 &&             met >= 250 && met < 400) return offset + 30;
        if (mT >= 160 &&             met >= 400             ) return offset + 31;
    }
    if(mll >= 105) {
        if (mT >=   0 && mT < 100 && met >=   0 && met < 100) return offset + 32;
        if (mT >=   0 && mT < 100 && met >= 100 && met < 150) return offset + 33;
        if (mT >=   0 && mT < 100 && met >= 150 && met < 200) return offset + 34;
        if (mT >=   0 && mT < 100 && met >= 200 && met < 250) return offset + 35;
        if (mT >=   0 && mT < 100 && met >= 250             ) return offset + 36;
        if (mT >= 100 && mT < 160 && met >=   0 && met < 100) return offset + 37;
        if (mT >= 100 && mT < 160 && met >= 100 && met < 150) return offset + 38;
        if (mT >= 100 && mT < 160 && met >= 150 && met < 200) return offset + 39;
        if (mT >= 100 && mT < 160 && met >= 200             ) return offset + 40;
        if (mT >= 160 &&             met >=   0 && met < 100) return offset + 41;
        if (mT >= 160 &&             met >= 100 && met < 150) return offset + 42;
        if (mT >= 160 &&             met >= 150 && met < 200) return offset + 43;
        if (mT >= 160 &&             met >= 200             ) return offset + 44;
    }
    return 0;
}

int SR4lGplot(float mT2Z, float met, float mZ2, int offset=0) {
    if(mT2Z > 450) return 5+offset;
    if(mT2Z > 300) return 4+offset;
    if(mT2Z > 150 && mZ2 < 60) return 3+offset;
    if(mT2Z > 150 && mZ2 >= 60) return 2+offset;
    if(mT2Z < 150) return 1+offset;
    return -1;
}

int unused4(int id1, int id2, int ord){
    int idx = 0;
    for (int i = 0; i< 4; i ++){
        if (i == id1 || i == id2){continue;}
        else idx++;
        if (idx == ord) return i;
    }
    return -1;
}

int SR4lHplot(float dRllH, float bestZ, int offset=0) {//Low MET CUT
    if(dRllH < 0.8) return 3+offset;
    if(dRllH > 0.8 && bestZ < 60) return 2+offset;
    if(dRllH > 0.8 && bestZ > 60) return 1+offset;
    return -1;
}


int SR_ewk_ss2l_v6_plot(float mt2, float met, float ptll, float ptdil, float mtW, float charge){
  int SR = 1;
  if (mt2 == 0){
      if (ptll < 70){
          if (met < 100) SR =  2;
          else if (met < 200 && charge > 0) SR =  3;
          else if (met < 200 && charge < 0) SR =  4;
          else if (charge > 0) SR =  5;
          else SR = 6;
      }
  }
  else if (mt2 < 80){
      if (ptdil < 30){
          if (met < 200 && charge > 0) SR = 7;
          else if (met < 200 && charge < 0) SR = 8;
          else if (charge > 0) SR = 9;
          else if (charge < 0) SR = 8;
      }
      else {
          SR=10;
      }
  }
  else if (mt2 >= 80){
      if (met < 100 && ptll < 200) SR = 11;
      else if (met < 200 && ptll < 200 && charge > 0) SR = 12;
      else if (met < 200 && ptll < 200 && charge < 0) SR = 13;
      else if (ptll < 200 && charge > 0) SR = 14;
      else if (ptll < 200 && charge < 0) SR = 15;
      if (ptll > 200){
          if (met < 100) SR =  16;
          else if (met < 200 && charge > 0) SR =  17;
          else if (met < 200 && charge < 0) SR =  18;
          else if (met < 900 && charge > 0) SR =  19;
          else if (met < 900 && charge < 0) SR =  20;
          else SR = 20;
      }
  }
  return SR;   
}

int SRC_new(float met, float mtZprime, float mt2ll){

    if (met < 200){
        if (mt2ll < 80) return 1;
        if (mt2ll < 120) return 2;
        else return 3;
    }
    else if (met > 200 && met < 300){
        if (mt2ll < 80) return 4;
        if (mt2ll < 120) return 5;
        return 6;
    }
    else if (met > 300){
        if (mtZprime < 250) return 7;
        if (mtZprime < 500) return 8;
        return 9;
    }
}


int SR3lD(float mT2L, float mT2T, float mll, float mT, float met, int offset = 0) {

    if(mT2L >= 0 && mT2L < 100){
        if(mll >=   0 && mll <  60 && met >=   0 && met < 100) return offset +  1;
        if(mll >=   0 && mll <  60 && met >= 100 && met < 150) return offset +  2;
        if(mll >=   0 && mll <  60 && met >= 150 && met < 200) return offset +  3;
        if(mll >=   0 && mll <  60 && met >= 200 && met < 250) return offset +  4;
        if(mll >=   0 && mll <  60 && met >= 250             ) return offset +  5;
        if(mll >=  60 && mll < 100 && met >=   0 && met < 100) return offset +  6;
        if(mll >=  60 && mll < 100 && met >= 100 && met < 150) return offset +  7;
        if(mll >=  60 && mll < 100 && met >= 150 && met < 200) return offset +  8;
        if(mll >=  60 && mll < 100 && met >= 200 && met < 250) return offset +  9;
        if(mll >=  60 && mll < 100 && met >= 250             ) return offset + 10;
        if(mll >= 100 &&              met >=   0 && met < 100) return offset + 11;
        if(mll >= 100 &&              met >= 100 && met < 150) return offset + 12;
        if(mll >= 100 &&              met >= 150 && met < 200) return offset + 13;
        if(mll >= 100 &&              met >= 200             ) return offset + 14;
    }
    if(mT2L >= 100) {
        if(met >=  0 && met < 200                            ) return offset + 15;
        if(met >= 200                                        ) return offset + 16;
    }

    return 0;
}


int SRE_new(float mt2, float mll, float met){
    if (mt2 < 80){
        if (mll < 50){
            if (met < 100) return 1;
            if (met < 250) return 2;
            else return 3;
        }
        else{
            if (met < 100) return 4;
            if (met < 250) return 5;
            else return 5;
        }
    }
    else{
        if (mll < 100){
            if (met < 150) return 6;
            else return 7;
        }
        else{
            if (met < 200) return 8;
            else return 9;
        }
    }
}


int SR3lF(float mT2L, float mT2T, float mll, float mT, float met, int offset = 0) {

    if(mT2T >= 0 && mT2T < 100){
        if(mll >=   0 && mll < 100 && met >=   0 && met < 100) return offset +  1;
        if(mll >=   0 && mll < 100 && met >= 100 && met < 150) return offset +  2;
        if(mll >=   0 && mll < 100 && met >= 150 && met < 200) return offset +  3;
        if(mll >=   0 && mll < 100 && met >= 200 && met < 250) return offset +  4;
        if(mll >=   0 && mll < 100 && met >= 250 && met < 300) return offset +  5;
        if(mll >=   0 && mll < 100 && met >= 300             ) return offset +  6;
        if(mll >= 100 &&              met >=   0 && met < 100) return offset +  7;
        if(mll >= 100 &&              met >= 100 && met < 150) return offset +  8;
        if(mll >= 100 &&              met >= 150 && met < 200) return offset +  9;
        if(mll >= 100 &&              met >= 200             ) return offset + 10;
    }
    if(mT2T >= 100) {
        if(met >=  0 && met < 200                            ) return offset + 11;
        if(met >= 200                                        ) return offset + 12;
    }

    return 0;
}

Bool_t allTight(float mva1, float mva2, float mva3, int pdg1, int pdg2, int pdg3, float cutmu, float cutel){
    if (abs(pdg1) == 11 && mva1 < cutel) return false; 
    if (abs(pdg1) == 13 && mva1 < cutmu) return false; 
    if (abs(pdg2) == 11 && mva2 < cutel) return false; 
    if (abs(pdg2) == 13 && mva2 < cutmu) return false; 
    if (abs(pdg3) == 11 && mva3 < cutel) return false; 
    if (abs(pdg3) == 13 && mva3 < cutmu) return false; 
    return true;
}


int encodepdg(int pdg1, int pdg2, int pdg3){
  int code1; int code2; int code3;
  if (pdg1 == 11) code1 = 0;
  if (pdg1 == -11) code1 = 1;
  if (pdg1 == 13) code1 = 2;
  if (pdg1 == -13) code1 = 3;
  if (pdg2 == 11) code2 = 0;
  if (pdg2 == -11) code2 = 1;
  if (pdg2 == 13) code2 = 2;
  if (pdg2 == -13) code2 = 3;
  if (pdg3 == 11) code3 = 0;
  if (pdg3 == -11) code3 = 1;
  if (pdg3 == 13) code3 = 2;
  if (pdg3 == -13) code3 = 3;
  return 16*code1+4*code2+code3;
}

int decodepdg(int enc, int pos){
  int rest;
  if (pos == 1) rest = (enc - enc%16)/16;
  if (pos == 2) rest = ((enc - enc%4)/4)%4;
  if (pos == 3) rest = enc%4;
  if (rest == 0) return 11;
  if (rest == 1) return -11;
  if (rest == 2) return 13;
  if (rest == 3) return -13;
}


float SR3lAfromlepgood(float metpt, float m12, float m13, float m23, float mt1, float mt2, float mt3, int encodedpdg){
  int pdg1 = decodepdg(encodedpdg,1);
  int pdg2 = decodepdg(encodedpdg,2);
  int pdg3 = decodepdg(encodedpdg,3);

  if (pdg1 == -pdg2){
    if (pdg1 != pdg3 && pdg2 != pdg3){
      return SR3lA(-1,-1,m12,mt3,metpt);
    }
    else if (pdg2 == pdg3){
      if (abs(m12 - 91.16) < abs(m13-91.16)) return  SR3lA(-1,-1,m12,mt3,metpt);
      else return SR3lA(-1,-1,m13,mt2,metpt);
    }
    else{
      if (abs(m12 - 91.16) < abs(m23-91.16)) return  SR3lA(-1,-1,m12,mt3,metpt);
      else return SR3lA(-1,-1,m23,mt1,metpt);
    }
  }
  else if (pdg1 == pdg2){
    if (pdg3 == -pdg1){
      if (abs(m13 - 91.16) < abs(m23-91.16)) return  SR3lA(-1,-1,m13,mt2,metpt);
      else return SR3lA(-1,-1,m23,mt1,metpt);
    }
    else return -1;
  }
  else if (pdg1 == -pdg3) return  SR3lA(-1,-1,m13,mt2,metpt);
  else if (pdg2 == -pdg3) return  SR3lA(-1,-1,m23,mt1,metpt);
  return -1;
}

Bool_t samesign(int pdg1, int pdg2){
  return pdg1*pdg2 > 0;
}

void functionsEWKcorr() {}
