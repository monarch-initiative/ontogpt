#!/usr/bin/perl
sqlite3 $db/omim.db -cmd "select subject,object from statements where predicate='IAO:0000142'" 
