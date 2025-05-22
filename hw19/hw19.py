'''
Вивести таблицю з найпопулярнішим та найменш популярним ім'ям для дівчаток та хлопчиків по кожному році.
baby_names.zip baby_names.zip14 березня 2024, 12:55 PM
'''

import os

def get_most_least_popular_names(data_dir, filename):
    filepath = os.path.join(data_dir, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()

    names_and_counts = [line.split() for line in lines]
    names, counts = zip(*names_and_counts)

    most_popular_name = names[counts.index(max(counts))]
    most_popular_count = max(counts)

    least_popular_name = names[counts.index(min(counts))]
    least_popular_count = min(counts)

    return most_popular_name, most_popular_count, least_popular_name, least_popular_count

def main():
    data_dir = "baby_names"  # Replace with your actual directory path

    for year in range(1900, 2013):
        boys_filename = f"{year}_BoysNames.txt"
        girls_filename = f"{year}_GirlsNames.txt"

        most_popular_boy_name, most_popular_boy_count, least_popular_boy_name, least_popular_boy_count = get_most_least_popular_names(data_dir, boys_filename)
        most_popular_girl_name, most_popular_girl_count, least_popular_girl_name, least_popular_girl_count = get_most_least_popular_names(data_dir, girls_filename)

        print(f"{year} | Хлопчики | {most_popular_boy_name} | {most_popular_boy_count} | {least_popular_boy_name} | {least_popular_boy_count} | Дівчата | {most_popular_girl_name} | {most_popular_girl_count} | {least_popular_girl_name} | {least_popular_girl_count}")

if __name__ == "__main__":
    main()

# 1900 | Хлопчики | John | 9830 | Ernest | 1012 | Дівчата | Beulah | 974 | Maude | 1013
# 1901 | Хлопчики | Paul | 924 | Fred | 1133 | Дівчата | Mamie | 992 | Blanche | 1025
# 1902 | Хлопчики | Joe | 955 | Roy | 1002 | Дівчата | Jennie | 985 | Katherine | 1004
# 1903 | Хлопчики | Roy | 975 | Raymond | 1051 | Дівчата | Lucy | 990 | Willie | 1014
# 1904 | Хлопчики | Joe | 959 | Raymond | 1093 | Дівчата | Leona | 998 | Stella | 1026
# 1905 | Хлопчики | Louis | 981 | Roy | 1017 | Дівчата | Ann | 996 | Bernice | 1032
# 1906 | Хлопчики | Ralph | 984 | Joe | 1020 | Дівчата | Jennie | 986 | Mamie | 1002
# 1907 | Хлопчики | Ralph | 998 | Earl | 1006 | Дівчата | Jennie | 998 | Betty | 1018
# 1908 | Хлопчики | Earl | 999 | Ernest | 1000 | Дівчата | Cora | 962 | Beulah | 1015
# 1909 | Хлопчики | Samuel | 983 | Earl | 1007 | Дівчата | Jennie | 998 | Opal | 1028
# 1910 | Хлопчики | Anthony | 980 | Francis | 1000 | Дівчата | Lula | 974 | Sylvia | 1000
# 1911 | Хлопчики | Stanley | 997 | Eugene | 1058 | Дівчата | Genevieve | 989 | Cora | 1022
# 1912 | Хлопчики | Victor | 989 | Sidney | 1002 | Дівчата | Mildred | 8764 | Ruth | 11276
# 1913 | Хлопчики | Maurice | 994 | Gordon | 1016 | Дівчата | Mildred | 9919 | Ruth | 12607
# 1914 | Хлопчики | Walter | 8961 | Irving | 1156 | Дівчата | Frances | 9676 | Elizabeth | 11365
# 1915 | Хлопчики | Richard | 9143 | Henry | 10139 | Дівчата | Lillian | 9546 | Florence | 10104
# 1916 | Хлопчики | Raymond | 9564 | Richard | 10133 | Дівчата | Rose | 9605 | Florence | 10411
# 1917 | Хлопчики | Raymond | 9960 | Henry | 10697 | Дівчата | Lillian | 9843 | Florence | 10538
# 1918 | Хлопчики | Donald | 9975 | Arthur | 10105 | Дівчата | Lillian | 9985 | Florence | 11317
# 1919 | Хлопчики | Donald | 9900 | Henry | 10617 | Дівчата | Irene | 9712 | Betty | 10106
# 1920 | Хлопчики | Jack | 9598 | Albert | 10002 | Дівчата | Louise | 9181 | Lillian | 10052
# 1921 | Хлопчики | Harry | 9729 | Albert | 10153 | Дівчата | Lillian | 9767 | Irene | 10626
# 1922 | Хлопчики | Albert | 9886 | Arthur | 10122 | Дівчата | Lillian | 9427 | Florence | 10038
# 1923 | Хлопчики | Arthur | 9921 | Henry | 11067 | Дівчата | Florence | 9748 | Irene | 10049
# 1924 | Хлопчики | Albert | 9881 | Arthur | 10172 | Дівчата | Irene | 9930 | Marjorie | 10064
# 1925 | Хлопчики | Arthur | 9981 | Kenneth | 10144 | Дівчата | Lois | 9572 | Shirley | 10514
# 1926 | Хлопчики | Henry | 9990 | Kenneth | 10337 | Дівчата | Lois | 9821 | Marie | 10632
# 1927 | Хлопчики | Henry | 9859 | Kenneth | 10850 | Дівчата | Irene | 8610 | Marie | 10307
# 1928 | Хлопчики | David | 9990 | Walter | 10646 | Дівчата | Dolores | 9614 | Alice | 10140
# 1929 | Хлопчики | Walter | 9855 | Kenneth | 10832 | Дівчата | Evelyn | 9881 | Mildred | 10251
# 1930 | Хлопчики | Walter | 9717 | Harold | 11652 | Дівчата | Joyce | 9657 | Lois | 10114
# 1931 | Хлопчики | Billy | 9259 | Harold | 10687 | Дівчата | Frances | 9716 | Nancy | 10031
# 1932 | Хлопчики | Billy | 9427 | Raymond | 10347 | Дівчата | Elizabeth | 9994 | Marilyn | 10568
# 1933 | Хлопчики | Jack | 9829 | Frank | 10953 | Дівчата | Jean | 9964 | Ruth | 11133
# 1934 | Хлопчики | Jack | 9984 | Frank | 10629 | Дівчата | Virginia | 9997 | Carol | 10270
# 1935 | Хлопчики | Raymond | 9560 | Frank | 10415 | Дівчата | Ruth | 9988 | Marilyn | 10416
# 1936 | Хлопчики | Raymond | 9451 | Frank | 10189 | Дівчата | Virginia | 9650 | Marilyn | 11064
# 1937 | Хлопчики | Raymond | 9574 | Frank | 10123 | Дівчата | Marilyn | 9735 | Helen | 11451
# 1938 | Хлопчики | Gerald | 9967 | Frank | 10250 | Дівчата | Janet | 9869 | Carolyn | 10586
# 1939 | Хлопчики | Frank | 9982 | Gerald | 10051 | Дівчата | Elizabeth | 9706 | Janet | 10113
# 1940 | Хлопчики | Raymond | 9565 | Gerald | 10236 | Дівчата | Elizabeth | 9955 | Janet | 10105
# 1941 | Хлопчики | Raymond | 9947 | Frank | 10784 | Дівчата | Helen | 9886 | Virginia | 10040
# 1942 | Хлопчики | Roger | 9175 | Raymond | 11109 | Дівчата | Marilyn | 9902 | Helen | 10012
# 1943 | Хлопчики | Daniel | 9165 | Roger | 10763 | Дівчата | Helen | 9799 | Marilyn | 10143
# 1944 | Хлопчики | Daniel | 9314 | Gerald | 10020 | Дівчата | Gloria | 9964 | Diane | 10710
# 1945 | Хлопчики | Raymond | 9854 | Roger | 10570 | Дівчата | Marilyn | 9534 | Elizabeth | 10336
# 1946 | Хлопчики | Steven | 8890 | Gerald | 10025 | Дівчата | Martha | 9759 | Virginia | 10018
# 1947 | Хлопчики | Douglas | 9905 | Wayne | 10165 | Дівчата | Linda | 99685 | Bonnie | 10218
# 1948 | Хлопчики | Gerald | 9825 | Mark | 10272 | Дівчата | Marilyn | 9929 | Martha | 10013
# 1949 | Хлопчики | Gerald | 9789 | Lawrence | 10230 | Дівчата | Marilyn | 9867 | Dorothy | 10408
# 1950 | Хлопчики | Gerald | 9729 | Lawrence | 10193 | Дівчата | Martha | 9831 | Beverly | 10510
# 1951 | Хлопчики | Anthony | 9828 | Lawrence | 10241 | Дівчата | Gail | 9885 | Kathy | 10398
# 1952 | Хлопчики | Peter | 9580 | Lawrence | 10284 | Дівчата | Marilyn | 9806 | Joan | 10261
# 1953 | Хлопчики | Lawrence | 9842 | Kevin | 10000 | Дівчата | Joan | 9770 | Marilyn | 10736
# 1954 | Хлопчики | Patrick | 9903 | Peter | 10068 | Дівчата | Gail | 9716 | Betty | 10618
# 1955 | Хлопчики | Patrick | 9861 | Brian | 10104 | Дівчата | Beverly | 9988 | Robin | 10219
# 1956 | Хлопчики | Michael | 90611 | Roger | 10144 | Дівчата | Cindy | 9987 | Cathy | 10141
# 1957 | Хлопчики | Roger | 9861 | Patrick | 10342 | Дівчата | Christine | 9577 | Joyce | 10150
# 1958 | Хлопчики | Michael | 90494 | Steve | 10077 | Дівчата | Tammy | 9979 | Christine | 10054
# 1959 | Хлопчики | Craig | 9918 | Patrick | 10554 | Дівчата | Judy | 9881 | Catherine | 10021
# 1960 | Хлопчики | Raymond | 9718 | Patrick | 10368 | Дівчата | Rebecca | 9970 | Laurie | 10147
# 1961 | Хлопчики | Steve | 9988 | Ricky | 10015 | Дівчата | Kelly | 9637 | Rebecca | 10237
# 1962 | Хлопчики | Frank | 9753 | Bruce | 10042 | Дівчата | Jacqueline | 9832 | Margaret | 10079
# 1963 | Хлопчики | Dennis | 9837 | Jerry | 10190 | Дівчата | Maria | 9817 | Paula | 10143
# 1964 | Хлопчики | Peter | 9904 | Randy | 10297 | Дівчата | Kim | 9985 | Maria | 10127
# 1965 | Хлопчики | Matthew | 9993 | Keith | 10685 | Дівчата | Stephanie | 9763 | Kim | 10081
# 1966 | Хлопчики | George | 9941 | Andrew | 10240 | Дівчата | Rhonda | 9803 | Stephanie | 10165
# 1967 | Хлопчики | Andrew | 9974 | Keith | 11006 | Дівчата | Rebecca | 9819 | Debra | 10225
# 1968 | Хлопчики | Keith | 9871 | Andrew | 10561 | Дівчата | Brenda | 9940 | Rebecca | 10227
# 1969 | Хлопчики | Keith | 9449 | Gary | 11153 | Дівчата | Denise | 9803 | Heather | 10072
# 1970 | Хлопчики | Keith | 9611 | Sean | 10366 | Дівчата | Donna | 9972 | Michele | 10095
# 1971 | Хлопчики | Keith | 9862 | Sean | 10512 | Дівчата | Christina | 9911 | Wendy | 10060
# 1972 | Хлопчики | Todd | 9991 | Andrew | 10127 | Дівчата | Patricia | 9606 | Christina | 10172
# 1973 | Хлопчики | Stephen | 9952 | Jonathan | 10272 | Дівчата | Tracy | 9909 | Laura | 10342
# 1974 | Хлопчики | Adam | 8433 | Stephen | 10104 | Дівчата | Christine | 9896 | Shannon | 10608
# 1975 | Хлопчики | Stephen | 9739 | Gregory | 10410 | Дівчата | Shannon | 9370 | Laura | 10316
# 1976 | Хлопчики | Adam | 9947 | Gregory | 10064 | Дівчата | Rachel | 8459 | Mary | 10326
# 1977 | Хлопчики | Nathan | 9885 | Gregory | 10053 | Дівчата | Andrea | 9784 | Erin | 10199
# 1978 | Хлопчики | Nathan | 9892 | Chad | 10115 | Дівчата | Rachel | 9806 | Mary | 10047
# 1979 | Хлопчики | Patrick | 9985 | Chad | 10154 | Дівчата | Tiffany | 9611 | Rachel | 10231
# 1980 | Хлопчики | Kenneth | 9612 | Stephen | 10068 | Дівчата | Shannon | 9667 | Andrea | 10452
# 1981 | Хлопчики | Kenneth | 9478 | Travis | 10107 | Дівчата | Kristin | 9737 | Danielle | 10029
# 1982 | Хлопчики | Dustin | 9548 | Jacob | 10050 | Дівчата | Kristen | 9535 | April | 10060
# 1983 | Хлопчики | Gregory | 9975 | Travis | 10475 | Дівчата | Mary | 9891 | Sara | 10083
# 1984 | Хлопчики | Gregory | 9685 | Sean | 10006 | Дівчата | Jamie | 9761 | Katherine | 10151
# 1985 | Хлопчики | Gregory | 9766 | Scott | 10137 | Дівчата | Erica | 9523 | Andrea | 10048
# 1986 | Хлопчики | Nathan | 9992 | Dustin | 10315 | Дівчата | Erica | 9971 | Erin | 10063
# 1987 | Хлопчики | Nathan | 9907 | Dustin | 10097 | Дівчата | Kelly | 9857 | Sara | 10084
# 1988 | Хлопчики | Samuel | 9550 | Nathan | 10145 | Дівчата | Erica | 9590 | Sara | 10008
# 1989 | Хлопчики | Dustin | 9719 | Samuel | 10103 | Дівчата | Sara | 9707 | Kimberly | 11035
# 1990 | Хлопчики | Jesse | 8973 | Jason | 10674 | Дівчата | Kelsey | 9494 | Kimberly | 10191
# 1991 | Хлопчики | Jeffrey | 9896 | Travis | 10134 | Дівчата | Kimberly | 9801 | Shelby | 10219
# 1992 | Хлопчики | Stephen | 9305 | Nathan | 10146 | Дівчата | Heather | 9724 | Alyssa | 10163
# 1993 | Хлопчики | Charles | 9855 | Sean | 10175 | Дівчата | Brianna | 8770 | Michelle | 10184
# 1994 | Хлопчики | Richard | 9513 | Nathan | 10381 | Дівчата | Kelsey | 9751 | Alexandra | 10224
# 1995 | Хлопчики | Timothy | 9784 | Nathan | 10302 | Дівчата | Rebecca | 9899 | Alyssa | 10098
# 1996 | Хлопчики | Steven | 9646 | Nathan | 10279 | Дівчата | Amber | 9771 | Alexandra | 10022
# 1997 | Хлопчики | Brian | 9732 | Cody | 10291 | Дівчата | Stephanie | 9777 | Morgan | 10342
# 1998 | Хлопчики | Eric | 9962 | Ethan | 10531 | Дівчата | Nicole | 9910 | Morgan | 10211
# 1999 | Хлопчики | Aaron | 9848 | Ethan | 11438 | Дівчата | Amanda | 9739 | Jennifer | 10609
# 2000 | Хлопчики | Caleb | 9857 | Kyle | 11964 | Дівчата | Destiny | 9842 | Sydney | 10242
# 2001 | Хлопчики | Aaron | 9529 | Jason | 10162 | Дівчата | Destiny | 9740 | Victoria | 10175
# 2002 | Хлопчики | Jason | 9953 | Elijah | 10049 | Дівчата | Victoria | 9775 | Anna | 10375
# 2003 | Хлопчики | Cameron | 9958 | Aidan | 10060 | Дівчата | Sophia | 9682 | Taylor | 10303
# 2004 | Хлопчики | Evan | 9973 | Connor | 10047 | Дівчата | Lauren | 9980 | Sophia | 10913
# 2005 | Хлопчики | Luke | 9999 | Thomas | 10029 | Дівчата | Chloe | 9582 | Natalie | 10727
# 2006 | Хлопчики | Justin | 9960 | Aidan | 10028 | Дівчата | Brianna | 9355 | Alyssa | 10167
# 2007 | Хлопчики | Luke | 9596 | Jordan | 10030 | Дівчата | Sarah | 9980 | Natalie | 10428
# 2008 | Хлопчики | Evan | 9912 | Isaac | 10007 | Дівчата | Alexis | 9708 | Mia | 10164
# 2009 | Хлопчики | Angel | 9832 | Landon | 10143 | Дівчата | Alexis | 9912 | Addison | 10650
# 2010 | Хлопчики | Evan | 9707 | Lucas | 10361 | Дівчата | Ella | 9864 | Elizabeth | 10225
# 2011 | Хлопчики | Caleb | 9973 | Jonathan | 10178 | Дівчата | Ella | 9553 | Elizabeth | 10024
# 2012 | Хлопчики | Isaac | 9928 | Nathan | 10357 | Дівчата | Elizabeth | 9596 | Madison | 11319
#
# Process finished with exit code 0

## Непогано! усміхаюсь