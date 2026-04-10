# Sample Support Incident

## Date

2026-04-09

## System

Internal support RAG assistant over product docs, runbooks, and incident history.

## Observations

- retrieved candidates often include the correct document family
- answers sometimes cite the previous or next section instead of the exact procedure
- engineers cannot consistently tell whether the issue is chunking, ranking, or answer assembly because chunk ids and citation anchors are not always logged

## Immediate Hypothesis

The system likely has a citation precision problem layered on top of acceptable candidate recall.
