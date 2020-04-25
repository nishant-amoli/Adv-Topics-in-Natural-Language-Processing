#!/usr/bin/perl

use warnings;
use strict;

my $filename = shift;
open(my $fh, '<', $filename)
    or die "Cannot open $filename $!";
my $line_count = 0;
while(<$fh>){
    $line_count++;
}

print "\n$filename has $line_count lines\n";
