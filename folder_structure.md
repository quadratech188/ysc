# Recommended Folder Structure for Research

This file outlines the recommended folder structure for conducting research with the GreenLight simulation software, especially when you need to modify the source code.

## Structure

```
/your_workspace/
├── GreenLight/      # Your forked and cloned GreenLight repository
│   ├── .git/
│   ├── greenlight/  # This is where you make your source code changes
│   ├── models/
│   ├── scripts/
│   └── ...
└── my_research/     # Your separate research project folder
    ├── data/
    │   ├── input_data/
    │   ├── output_data/
    │   └── raw_data/
    ├── models/
    ├── notebooks/
    ├── results/
    │   ├── figures/
    │   └── tables/
    ├── scripts/
    │   ├── analysis/
    │   └── simulation/
    └── README.md
```

## Workflow Summary

1.  **Fork and Clone**: Fork the `GreenLight` repository and clone your fork to your local machine. This is your development environment.
2.  **Editable Install**: Install the `GreenLight` package in editable mode (`pip install -e .`) from within the `GreenLight` directory.
3.  **Separate Research Folder**: Create a separate `my_research` folder outside the `GreenLight` repository to store your research-specific files (data, scripts, results).
4.  **Import**: Your research scripts in `my_research/scripts/` can import and use the modified `GreenLight` module.
