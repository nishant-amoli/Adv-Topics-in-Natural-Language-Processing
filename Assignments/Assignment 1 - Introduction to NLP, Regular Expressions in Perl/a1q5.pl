#!/usr/bin/perl

use warnings;
use strict;

my $line_count = 0;
my $line_len = 0;
my $shortest_line_length = 0;
my $longest_line_length = 0;
my $first_flag = 1;
while(<>){
    $line_count++;
    $_ =~ s/(\s)*\n$//g;
    $line_len = length($_);
    if($first_flag == 1){
	$shortest_line_length = $line_len;
	$longest_line_length = $line_len;
	$first_flag = 0;
    }else{
	if ($shortest_line_length > $line_len){
	    $shortest_line_length = $line_len;
	}
	if ($longest_line_length < $line_len){
	    $longest_line_length = $line_len;
	}
    }
}
print "\nnumber of lines: $line_count";
print "\nshortest line length: $shortest_line_length";
print "\nlongest line length: $longest_line_length\n";
