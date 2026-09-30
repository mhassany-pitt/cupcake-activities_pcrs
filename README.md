# Cupcake PCRS Free-Coding Activities

Auto-graded programming and free-coding practice activities adapted from the **Programming Class Research System (PCRS)** developed at the University of Toronto (Andrew Petersen et al.) and enriched through the ADAPT / Smart Learning Content (SLC) Catalog:

https://adapt2.sis.pitt.edu/next.course-authoring/#/catalog-v2

## Contents

This repository contains **473 free-coding activities** conforming to the Cupcake `free-coding/0.1.0` specification:

- **Authored & Curated by Leading Researchers**: Developed and curated by Kamil Akhuseyinoglu, Jordan Barria-Pineda, Roya Hosseini, Arun Balajiee Lekshmi Narayanan (University of Pittsburgh) and Andrew Petersen (University of Toronto).
- **Language Separation**: Partitioned into subdirectories by programming language:
  - `python/` (**328 activities**): Python 3 practice covering functions, string manipulation, dictionary and list operations, matrix algorithms, sorting, recursion, file handling, and introductory algorithmic challenges.
    - **Bilingual Coverage**: Includes 178 English activities and 150 localized Spanish (`es`) exercises (`_es.yaml`).
  - `java/` (**145 activities**): Core Java (Java 17) covering object-oriented design, linked lists, arrays, loops, recursion, conditionals, and data structures.
- **Segmented Editor Regions**: Faithful translation of PCRS's tagging architecture (`[blocked]` and `[student_code]`) into Cupcake's `elements` specification (`type: locked` for read-only boilerplate/wrapper code and `type: editable` for starter student code with placeholder guidance).
- **Clean Markdown Statements**: Extracted problem statements cleaned into clean Markdown with code fences, syntax highlighting, and stripped extraneous platform styles/tags.
- **Complete Metadata & Topics**: Includes academic author attribution, difficulty level (`novice`), and knowledge component topics namespaced by concept (`pcrs:<concept>`).

## Layout

```
python/
  ├── py_reverse_dict/
  │   ├── main.py
  │   └── py_reverse_dict_en.yaml
  └── py_avg_two_int_es/
      ├── main.py
      └── py_avg_two_int_es.yaml

java/
  ├── linkedlist_merge_no_feedback/
  │   ├── LinkedListExample.java
  │   └── linkedlist_merge_no_feedback_en.yaml
  └── recursion_power_no_feedback/
      ├── SCode.java
      └── recursion_power_no_feedback_en.yaml
```
