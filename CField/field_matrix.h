#ifndef _FIELD_MATRIX_H_
#define _FIELD_MATRIX_H_

mpz_t ** field_init_matrix(unsigned int n, unsigned int m)
{
  unsigned int i = 0, j = 0;
  mpz_t **A = calloc(n, sizeof(mpz_t*));
  for (i = 0; i < n; i++)
  {
    A[i] = calloc(m, sizeof(mpz_t));
    for (j = 0; j < m; j++)
      mpz_init(A[i][j]);
  }

  return A;
}

int field_read_matrix(mpz_t **A, unsigned int n, unsigned int m, char *filename)
{
  FILE *f = fopen(filename, "r");
  unsigned int i,j;
  unsigned long long c = 0;
  for (i = 0; i < n; i++)
    for (j = 0; j < m; j++)
    {
      fscanf(f, "%llu", &c);
      mpz_import(A[i][j], 1, -1, sizeof(c), 0, 0, &c);
    }
  fclose(f);
}

int field_print_matrix(mpz_t **A, unsigned int n, unsigned int m)
{
  unsigned int i,j;
  for (i = 0; i < n; i++)
  {
    for (j = 0; j < m; j++)
    {
      mpz_out_str(stdout, 10, A[i][j]);
      printf(" ");
    }
    printf("\n");
  }
  printf("\n");
}

int field_print_vec(mpz_t *vec, unsigned int n)
{
  unsigned int i;
  for (i = 0; i < n; i++)
  {
    mpz_out_str(stdout, 10, vec[i]);
    printf(" ");
  }
  printf("\n");
}

int field_clear_matrix(mpz_t **A, unsigned int n, unsigned int m)
{
  unsigned int i = 0, j = 0;
  for (i = 0; i < n; i++)
  {
    for (j = 0; j < m; j++)
      mpz_clear(A[i][j]);
    free(A[i]);
  }
  free(A);
}

void field_mul_matrix(mpz_t **C, mpz_t**A, unsigned long long na, unsigned long long ma, mpz_t **B, unsigned long long nb, unsigned long long mb)
{

  if (ma != nb)
  {
    printf("Can not mul matrix: diff sizes\n");
    exit(1);
  }
  mpz_t s;
  unsigned int i = 0, j = 0, k = 0;
  mpz_init(s);
  for (i = 0; i < na; i++)
  {
    for (j = 0; j < mb; j++)
    {
      for (k = 0; k < ma; k++)
      {
        field_mult(s, A[i][k], B[k][j]);
        field_add(C[i][j], C[i][j], s);
      }
    }
  }
  mpz_clear(s);
}

void field_transpose_matrix(mpz_t ** A, unsigned long long n, unsigned long long m)
{
  unsigned long long i = 0, j = 0;
  for(i = 0; i < n; i++)
    {
      for(j = i; j < m; j++)
      {
        mpz_swap(A[i][j], A[j][i]);
      }
    }
}

#endif
