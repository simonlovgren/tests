#include <stdio.h>
#include <limits.h>
#include <math.h>
#include "swedish.h"

heltal huvudfunktion(heltal argn, bokstav *argument) {
  heltal h = 5;
  medan(h > 0) {
    om(h == 3) {
      skrivs("treeee");
    } eller (h == 2) {
      skrivs("tvåååå");
    } annars {
      skrivf("Hej Världen!\n");
    }
    --h;
  }

  skrivf("Största värdet i en bokstav: %d\n", BOKST_MAX);
  skrivf("Kvadratroten av två upphöjt till 1.5: %f\n", kvdr(upph(2,1.5)));
  
  returnera 0;
}
