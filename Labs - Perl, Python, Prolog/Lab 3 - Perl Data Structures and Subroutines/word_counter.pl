#!/usr/bin/perl

use warnings;
use strict;

my %f = ();
my $tot = 0;

while(<>){
    while (/'?[a-zA-Z]+/g){
	$f{lc $&}++;
	$tot++;
    }
}

my $counter = 0;
print "\n10 most common words are:\n";
for (sort{ $f{$b} <=> $f{$a} } keys %f){
    if ($counter == 10) { print "\n"; last; }
    $counter++;
    print "$_ ";
}

my $legomena_count = 0;
for(keys %f){
    if($f{$_} == 1){
	$legomena_count++;
    }
}
print "\nThe number of hapax legomena is $legomena_count\n";

