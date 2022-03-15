#!/usr/bin/env ruby
require 'csv'

class CSVAnalyzer
  attr_accessor :csv_data, :file_path, :table_height, :table_width

  def initialize(file_path)
    @data_types = []
    @averages = []
    @medians = []
    @column_widths = []
    @csv_data = []
    @file_path = file_path
    load_csv_file
    @table_height = 6
    @table_width = 5
  end

  def command_operations(command)
    case command
     when "-d"
       display_data
     when "-m"
       display_median
     when "-a"
       display_average
     else
       raise ArgumentError, "Invalid command."
    end
  end

  def display_data
    set_table_size
    define_column_widths

    display_border
    display_rows(0, 1)
    display_border
    display_rows(1, @table_height)
    display_abbreviated_rows if @csv_data.length > @table_height
    display_border
  end

  def display_median
    find_each_median
    0.upto(@csv_data[0].length - 1) { |i| puts "#{@csv_data[0][i]}: #{@medians[i]}"}
  end

  def display_average
    find_data_types
    find_averages
    0.upto(@csv_data[0].length - 1) { |i| puts "#{@csv_data[0][i]}: #{@averages[i]}" }
  end

  private

  def load_csv_file
    file_path_validity_check
    @csv_data = CSV.read(@file_path)
    raise LoadError, "File is empty." if @csv_data.empty?
  end

  def file_path_validity_check
    raise LoadError, "Invalid file format" unless @file_path =~ /\.csv$/
    raise LoadError, "Invalid path." unless File.exist?(@file_path)
  end

  def set_table_size
    @table_height = csv_data.length if @csv_data.length < @table_height
    @table_width = csv_data[0].length if @csv_data[0].length < @table_width
  end

  def display_rows(lower_bound, upper_bound)
    (lower_bound..(upper_bound-1)).each do |i|
      (0..(@table_width - 1)).each do |j|
        # Prints the content of each cell
        print "|" + @csv_data[i][j] + " "*(@column_widths[j] - @csv_data[i][j].length)
      end
      # Prints the right border of the table with respect
      # to the size of the data set.
      @csv_data[0].length > @table_width ? (puts "|...|") : (puts "|")
    end
  end

  def display_border
    0.upto(@table_width - 1) { |width| print "+" + "-"*@column_widths[width] }
    @csv_data[0].length > @table_width ? (puts "+---+") : (puts "+")
  end

  def display_abbreviated_rows
    0.upto(2) do
      0.upto(@table_width - 1) do |i|
        print "|"
        # Sets the position for the dot for abbreviating
        # to be in the center of the column.
        dot_position = @column_widths[i] % 2 == 0 ? @column_widths[i]/2 : (@column_widths[i]/2 + 1)
        0.upto(@column_widths[i] - 1) do |column_position|
          column_position == dot_position - 1 ? (print ".") : (print " ")
        end
      end
      # Displays the right border of the table with respect to the
      # size of the data set.
      @csv_data[0].length > @table_width ? (puts "|...|") : (puts "|")
    end
  end

  def define_column_widths
    @column_widths = []
    (0..@table_width - 1).each { @column_widths.push(0) }

    # Finds the longest element within each column and stores it
    # within @column_widths.
    (0..@table_height).each do |i|
      (0..(@table_width - 1)).each do |j|
        @column_widths[j] = @csv_data[i][j].length if @csv_data[i][j].length > @column_widths[j]
      end
    end
  end

  def find_data_types
    (0..(@csv_data[0].length - 1)).each do |i|
      (1..(@csv_data.length - 1)).each do |j|
        next if @csv_data[j][i] == ""
        if !(@csv_data[j][i] =~ /^(\d+)?(\.\d*)?$/) || @csv_data[j][i] =~ /^\.$/
          @data_types.push(:categorical)
          break
        end
      end
      @data_types.push(:numerical) if @data_types.length == i
    end
  end

  def find_median(data_count)
    data = []
    counts = []

    data_count.each do |key,value|
      data.push(key)
      counts.push(value)

      if data.length > 1
        if counts[-1] > counts[-2]
          (data.length - 1).downto(1) do |index|
            if counts[index] > counts[index-1]
              switch_position(data, index)
              switch_position(counts, index)
            else
              break
            end
          end
        end
      end

    end
    data[0]
  end

  def switch_position(array,index)
    temp = array[index-1]
    array[index-1] = array[index]
    array[index] = temp
  end

  def find_each_median
    # Loop that goes through the columns then
    # the rows of csv_data.
    (0..(@csv_data[0].length - 1)).each do |i|
      data_count = {}
      (1..(@csv_data.length - 1)).each do |j|
        next if @csv_data[j][i] == ""

        if data_count.keys.include?(@csv_data[j][i])
          data_count[@csv_data[j][i]] += 1
        else
          data_count[@csv_data[j][i]] = 1
        end
      end
      @medians.push(find_median(data_count))
    end
  end

  def find_averages
    (0..(@csv_data[0].length - 1)).each do |i|
      if @data_types[i] == :categorical
        @averages.push("Not applicable")
        next
      end
      sum = 0.0
      point_counter = 0.0
      (1..(@csv_data.length - 1)).each do |j|
        next if @csv_data[j][i] == ""
        sum += @csv_data[j][i].to_f
        point_counter += 1
      end
      @averages.push((sum/point_counter).round(2).to_s)
    end
  end
end

if __FILE__ == $0
  if ARGV.empty?
    puts <<END
< Help >
Gives the details of a csv file.

use: [option] [.csv file path]

options:
[-d]: Displays data
[-m]: Display median
[-a]: Display average
END
  raise ArgumentError, "No arguments passed."
  end

  raise ArgumentError, "Too many arguments." if ARGV.length > 2
  raise ArgumentError, "Too few arguments," if ARGV.length  == 1

  csv_analyzer = CSVAnalyzer.new(ARGV[1])
  csv_analyzer.command_operations(ARGV[0])
end
