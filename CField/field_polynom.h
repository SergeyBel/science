#ifndef _FIELD_POLYNOM_H_
#define _FIELD_POLYNOM_H_



int polynom_value(mpz_t y, mpz_t* polynom, unsigned int n, mpz_t x)
{
  long long i = 0;
  mpz_init_set(y, polynom[n - 1]);
  for(i = n - 2; i >= 0; i--)
  {
    field_mult(y, y, x);
    field_add(y, polynom[i], y);
  }
}

#endif
