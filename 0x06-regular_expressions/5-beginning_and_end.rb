#!/usr/bin/env ruby
matches = ARGV[0].scan(/h.n/)
puts matches.join unless matches.empty?
