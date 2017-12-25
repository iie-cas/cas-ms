Models = {
    """
    CREATE TABLE IF NOT EXISTS admin (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        account VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL,
        username VARCHAR(100) NOT NULL,
        is_super TINYINT DEFAULT 0,
        create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY(id)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """
    ,
    """
    CREATE TABLE IF NOT EXISTS user (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        account VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL,
        username VARCHAR(100) NOT NULL,
        education VARCHAR(100) NOT NULL,
        grade VARCHAR(100) NOT NULL,
        score INT DEFAULT 0,
        fund INT DEFAULT 0,
        telephone VARCHAR(100),
        qq VARCHAR(100),
        adm_time VARCHAR(100),
        create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY(id)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """
    ,
    """
    CREATE TABLE IF NOT EXISTS scorelog (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        user_id INT UNSIGNED NOT NULL,
        value INT NOT NULL,
        reason VARCHAR(500) NOT NULL,
        update_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY(id),
        FOREIGN KEY(user_id) REFERENCES user(id)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """
    ,
    """
    CREATE TABLE IF NOT EXISTS fundlog (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        user_id INT UNSIGNED NOT NULL,
        value INT NOT NULL,
        reason VARCHAR(500) NOT NULL,
        update_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY(id),
        FOREIGN KEY(user_id) REFERENCES user(id)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """
    ,
    """
    CREATE TABLE IF NOT EXISTS score_label (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        PRIMARY KEY(id)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """
}