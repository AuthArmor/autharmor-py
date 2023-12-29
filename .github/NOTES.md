## Generation
```python
openapi-generator-cli generate --generator-name python --input-spec openapi.json --output sdk  --package-name autharmor_python --package-version 1.2.3
```

## Build
- Install pypa beforehand https://github.com/pypa/build
- python -m build

## Deploy
py -m twine upload --repository testpypi ./dist/* --verbose

## Deployment Flow

1. On git push, AZ pipeline is started
2. AZ pipeline will delete any sdk folder
3. AZ pipeline will then generate via the above a new package with the version number collected from the user (in AZ admin)
4. AZ pipeline will move then update some lines in setup.py then:
5. Deploy to test pypi to test, then if all correct:
6. Deploy to prod pypi to complete.
7. Execute installs from testpypi and pypi itself to test installs.