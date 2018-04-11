# celebration  a group of children of varying ages, split them up into groups, within the group the
# ages can not be greater than 1 year.  Minimize the number of groups

def group_children_age_diff_no_more_than_a_year(kids):
    '''group children exercise'''
    groups = set()
    i = 0
    while i < len(kids) - 1:
        group = () # tuple, since you can't add list to set, since list is not immutable
        youngest = kids[i]
        print('youngest {}'.format(youngest))
        #group = group + (i,)
        group = group + (kids[i],)

        while i+1 < len(kids) and kids[i+1] - youngest <= 1:
            #group = group + (i + 1,)
            group = group + (kids[i + 1],)
            i += 1

        groups.add(group)
        i += 1

    return groups


children = [2, 2.6, 3.5, 4, 5, 6]
print(group_children_age_diff_no_more_than_a_year(children))
