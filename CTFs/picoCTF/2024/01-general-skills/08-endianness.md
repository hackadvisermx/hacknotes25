
Know of little and big endian?

Additional details will be available after launching your challenge instance.

- You might want to check the ASCII table to first find the hexadecimal representation of characters before finding the endianness.
- Read more about how endianness [here](https://levelup.gitconnected.com/little-endian-and-big-endian-74ab6441b2a7)

## Solve

```
castr@mymac endianness % nc titan.picoctf.net 63999
Welcome to the Endian CTF!
You need to find both the little endian and big endian representations of a word.
If you get both correct, you will receive the flag.
Word: tvcov
Enter the Little Endian representation: 766F637674%
Correct Little Endian representation!
Enter the Big Endian representation: Incorrect Big Endian representation. Try again!
Enter the Big Endian representation: 7476636f76
Correct Big Endian representation!
Congratulations! You found both endian representations correctly!
Your Flag is: picoCTF{3ndi4n_sw4p_su33ess_02999450}
```

- modificar el programa para que este mismo nos de las respuestas

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>
#include <time.h>

char *find_little_endian(const char *word)
{
    size_t word_len = strlen(word);
    char *little_endian = (char *)malloc((2 * word_len + 1) * sizeof(char));

    for (size_t i = word_len; i-- > 0;)
    {
        snprintf(&little_endian[(word_len - 1 - i) * 2], 3, "%02X", (unsigned char)word[i]);
    }

    little_endian[2 * word_len] = '\0';
    return little_endian;
}

char *find_big_endian(const char *word)
{
    size_t length = strlen(word);
    char *big_endian = (char *)malloc((2 * length + 1) * sizeof(char));

    for (size_t i = 0; i < length; i++)
    {
        snprintf(&big_endian[i * 2], 3, "%02X", (unsigned char)word[i]);
    }

    big_endian[2 * length] = '\0';
    return big_endian;
}

int main()
{

    //char *little_endian = find_little_endian(challenge_word);
    size_t user_little_endian_size = 5;
    char user_little_endian[user_little_endian_size + 1];

    printf("Word ?:  ");
    fflush(stdout);
    scanf("%10s", user_little_endian);

     char *little_endian = find_little_endian(user_little_endian);
     char *big_endian = find_big_endian(user_little_endian);

     printf("%s\n",little_endian);
     printf("%s\n",big_endian);


    return 0;
}
```

## Referencias

- https://levelup.gitconnected.com/little-endian-and-big-endian-74ab6441b2a7
- 