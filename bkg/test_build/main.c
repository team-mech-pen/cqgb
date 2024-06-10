#include <gb/gb.h>

extern int bkg_pattern_table_size;
extern char * bkg_pattern_table;
extern char * bkg_index_table;


int main()
{
    set_bkg_data(0, bkg_pattern_table_size, bkg_pattern_table);
    set_bkg_tiles(0, 0, 20, 18, bkg_index_table);
    SHOW_BKG;
    return 0;
}