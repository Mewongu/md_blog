---
    author: Andreas Stenberg
    title: "Building This: The Concept (Part 2)"
    url: building_this_p2_the_concept
    keywords: 
        - Development
        - Blog
---

How does one keep a blog platform simple? Seems to me that every time I write a blog platform it explodes into this mess of small services and ideas. Suddenly everything has lost purpose because the only focus is developing the next feature instead of fixing problems in the existing parts. This project feels more well thougt out. Everything is handled in git. The code as well as the articles and templates. 

### Articles
What does an article contain? What information is required by an author? The plan is to require as little as possible. An article needs a title. It could be written in markdown however this feels a bit awkward since there would need to exist some code that would parse out the title from the markdown. Instead it is placed as info in YAML frontmatter of the markdown file. Furthermore the frontmatter contains:

|Attribute|Description|
|:---|:---|
|title|The title of the article/post|
|url|The url extension for the specific post. Needs to be unique for every article.|
|keywords|A list of keywords. These wil be used as tags in the future|

Additional interesting information could be the author, post creation date and latest edit date. It would however go against the idea of keeping it simple to need to maintain this information in the YAML. Instead this information will be gathered based on git. Author will be the authors of the commits touching the specific article. Initial creation date will be the same date as when the article was first commited into git and the edit date will be the last time it was commited into git if applicable. 

### Users
None or as many as one wants. Since author information is gathered based on git info a Pull-Request could lead to a post authored by someone new. 

### Series
A series is a series of articles grouped by a folder. Certain behaviour should implicitly happen due to folder structure. An example:

Currently there are two articles written. "Building This: New Beginnings" and "Building This: The Concept". These are meant to be linked together but currently that is performed via updating the "Series" part of the articles every time a new article is written or a title changed. This should instead be done by placing them in a folder named "Building This". It should automatically link to the other articles in the series by doing this. I will need to implement this soon. 

### Tags/Keywords
Metadata is added through the YAML of articles as previously metioned. What is not mentioned is that tags, or if one wishes to call them keywords, should be accesible via a tagged link. E.g. Visiting `/tags/development` should bring a user to all articles regarding development. This also needs implementation. 

### This series

1) [Building This: New Beginnings (Part 1)](/building_this_p1_new_beginnings)  
2) [Building This: The Concept (Part 2)](/building_this_p2_the_concept)