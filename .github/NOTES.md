## Generation
```python
openapi-generator-cli generate --generator-name python --input-spec openapi.json --output sdk  --package-name autharmor_python 
```

## Build
- Install pypa beforehand https://github.com/pypa/build
- python -m build

## Deploy
py -m twine upload --repository testpypi ./dist/* --verbose 