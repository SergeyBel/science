#ifndef _FIELD_H_
#define _FIELD_H_

#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <stdint.h>
#include <assert.h>
#include <time.h>
#include <gmp.h>

mpz_t irred_coeff[128];
unsigned long long degree;
mpz_t poly;

void irred_coeff_set()
{
  mpz_init_set_ui(irred_coeff[2], 7);
  mpz_init_set_ui(irred_coeff[3], 13);
  mpz_init_set_ui(irred_coeff[4], 19);
  mpz_init_set_ui(irred_coeff[8], 285);
  mpz_init_set_ui(irred_coeff[16], 65581);
  mpz_init_set_str(irred_coeff[32], "4295000729", 10);
  mpz_init_set_str(irred_coeff[33], "8589950281", 10);
  mpz_init_set_str(irred_coeff[64], "10000400000000013", 16);
  //mpz_init_set_str(irred_coeff[64], "10000000247F43CB7", 16);
}

#define mpz_lshift(A, B, l) mpz_mul_2exp(A, B, l)l
#define mpz_sizeinbits(A) (mpz_cmp_ui(A, 0) ? mpz_sizeinbase(A, 2) : 0)



void field_init(unsigned int n)
{
  irred_coeff_set();
  mpz_set(poly, irred_coeff[n]);
  degree = n;
}

void field_deinit(void)
{
    mpz_clear(poly);
}

void field_add(mpz_t z, const mpz_t x, const mpz_t y)
{
    mpz_xor(z, x, y);
}

void field_mult(mpz_t z, const mpz_t x, const mpz_t y)
{
    mpz_t b;
    unsigned int i;
    mpz_init_set(b, x);
    if (mpz_tstbit(y, 0))
        mpz_set(z, b);
    else
        mpz_set_ui(z, 0);


    for(i = 1; i < degree; i++)
    {
        mpz_lshift(b, b, 1);
        if (mpz_tstbit(b, degree))
            mpz_xor(b, b, poly);
        if (mpz_tstbit(y, i))
            mpz_xor(z, z, b);
    }
    mpz_clear(b);
}

void field_invert(mpz_t z, const mpz_t x)
{
  if (!mpz_cmp_ui(x, 0))
  {
    printf("Error: invert 0\n");
    exit(1);
  }
    mpz_t u, v, g, h;
    int i;
    mpz_init_set(u, x);
    mpz_init_set(v, poly);
    mpz_init_set_ui(g, 0);
    mpz_set_ui(z, 1);
    mpz_init(h);
    while (mpz_cmp_ui(u, 1))
    {
        i = mpz_sizeinbits(u) - mpz_sizeinbits(v);
        if (i < 0)
        {
            mpz_swap(u, v);
            mpz_swap(z, g);
            i = -i;
        }
        mpz_lshift(h, v, i);
        mpz_xor(u, u, h);
        mpz_lshift(h, g, i);
        mpz_xor(z, z, h);
    }
    mpz_clear(u);
    mpz_clear(v);
    mpz_clear(g);
    mpz_clear(h);
}

void field_pow(mpz_t z, const mpz_t x, unsigned long long n)
{
  mpz_t y, c;
  mpz_set_ui(z, 1);
  mpz_init(c);
  mpz_init_set(y, x);
  while (n)
  {
    if (n & 1)
      field_mult(z, z, y);

    field_mult(c, y, y);
    mpz_set(y, c);
    n = n >> 1;
  }
  mpz_clear(y);
  mpz_clear(c);
}

void field_print(mpz_t x)
{
  mpz_out_str(stdout, 10, x);
  printf("\n");
}

#endif
