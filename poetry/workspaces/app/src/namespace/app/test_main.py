def test_import():
    from namespace.app.main import main  # type: ignore
    main(1)
