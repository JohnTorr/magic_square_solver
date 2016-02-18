"""
Magic square

# # #
# # #
# # #

Numbers 1 to 9
Rows add to 15
Cols add to 15
Diag add to 15

Solution finder
"""
# Make a loop to go through all number sequences
# for each of the 9 tiles
for i in range(0, 999999999):

    # Pad out number with 0's to have 9 tiles
    # This is the grid, It gets filled from the current loop
    nums = str(i).zfill(9)

    # Check no number has been duplicated
    # if the set doesn't have 9 members then some were dups
    if len(set(nums)) == 9:

        # Check Rows add to 15
        if ( int(nums[0]) + int(nums[1]) + int(nums[2]) ) == 15:
            if ( int(nums[3]) + int(nums[4]) + int(nums[5]) ) == 15:
                if ( int(nums[6]) + int(nums[7]) + int(nums[8]) ) == 15:
      
                    # Check Cols add to 15
                    if ( int(nums[0]) + int(nums[3]) + int(nums[6]) ) == 15:
                        if ( int(nums[1]) + int(nums[4]) + int(nums[7]) ) == 15:
                            if ( int(nums[2]) + int(nums[5]) + int(nums[8]) ) == 15:

                                # Check Diags add to 15
                                if ( int(nums[0]) + int(nums[4]) + int(nums[8]) ) == 15:
                                    if ( int(nums[6]) + int(nums[4]) + int(nums[2]) ) == 15:
        
                                        # Successful combination
                                        print( nums )



'''
# Solutions
276951438
294753618
438951276
492357816
618753294
672159834
816357492
834159672

'''
