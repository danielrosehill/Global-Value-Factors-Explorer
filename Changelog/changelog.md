# Changelog - Derivative Dataset

## Data formatting modifications

- Dolllar symbols were removed from the original dataset. The currency will be noted instead in manifest fields for each topic.

## Metadata

- Non-data elements were added as JSON files nested within each subject.

For example:

```
{
  "Name": "Water Pollution Value Factors",
  "Methodology Status": "Interim",
  "Update Date": "October 15, 2024",
  "Price Year": 2023,
  "Currency": "USD"
}
```