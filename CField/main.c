#include "field.h"
#include "field_matrix.h"
#include "field_polynom.h"


int main(int argc, char *argv[])
{
  unsigned int n = 2;
  mpz_t x, y, z;
  field_init(n);
  mpz_init_set_ui(x, 2);
  mpz_init_set_ui(y, 3);
  mpz_init(z);
  field_mult(z, x, y);
  field_print(z);
  mpz_clear(x);
  mpz_clear(y);
  mpz_clear(z);
  field_deinit();
  return 0;
}
