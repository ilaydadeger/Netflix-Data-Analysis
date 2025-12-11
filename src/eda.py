def show_basic_info(df):
    """
    Veri çerçevesinin temel bilgilerini gösterir.
    """
    print("===== BASIC INFO =====")
    print(df.info())
    print("\n===== NULL VALUES =====")
    print(df.isnull().sum())
    print("\n===== DESCRIPTIVE STATS =====")
    print(df.describe(include="all"))
