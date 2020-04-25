#!/usr/bin/perl

use warnings;
use strict;

#Subroutine that returns concatenated string
sub conc{
    my $str1 = shift;
    my $str2 = shift;
    
    #If string 1 is lexically smaller than string 2.
    if (($str1 cmp $str2) < 0){
	return $str1.$str2;
    }

    #If string 2 is lexically smaller than string 1.
    else{
	return $str2. $str1;
    }
}

print &conc('aaa','ccc');
print "\n";
print &conc('ccc','aaa');
print "\n";
