#include "main.h"

void jack_bauer(void)
{
    int hd = 0, hu = 0, md = 0, mu = 0;

    for (hd = '0'; hd <= '2'; hd++)
        for (hu = '0'; hu <= '9'; hu++)
            for (md = '0'; md <= '5'; md++)
                for(mu = '0'; mu <= '9'; mu++)
                {
                    if (hd != '2' || hu < '4')
                        {
                            putchar(hd);
                            putchar(hu);
                            putchar(':');
                            putchar(md);
                            putchar(mu);
                            putchar('\n');
                        }
                }

}