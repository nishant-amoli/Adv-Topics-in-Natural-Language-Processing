#!/usr/bin/perl
use strict;
use warnings;

my %f = ();
my $tot = 0;
while(<>){
    while (/\w+/){
	my $l = $&;
	$_ = $';
	$f{lc $l}++;
	$tot++;
    }
}

sub f{
    my $ref = shift;
    my $word = shift;
    if(exists(${$ref}{$word})){
	return ${$ref}{$word};
    }
 }
my $re = \%f;
my $freq = f($re,'tom');
print("\nThe frequency of the word Tom is $freq\n");
