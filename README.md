# PKUAutoElective 2022 Spring Version

**Update at Feb 22 12:49 (UTC+8)**: 针对@tainblit提出的`NoneType' object has no attribute 'tobytes'`问题进行了修改

**Update at Feb 20 11:32 (UTC+8)**: 修改了 `get_supplement` 和 `get_supplyCancel` 的 API 参数，已经可以实现课程列表页面的正常跳转，请更新至最新 commit 版本

-----

本项目基于 [PKUAutoElective](https://github.com/zhongxinghong/PKUAutoElective)，对 2021 春季学期的选课网站 API 改动进行了调整。并针对验证码系统的改动，将识别系统转为在线商用平台 [TT识图](http://www.ttshitu.com)（打钱！打钱！），**目前识别准确度欠佳**

## 安装

请参考 [PKUAutoElective](https://github.com/zhongxinghong/PKUAutoElective#安装) 项目提供的安装指南进行安装，但本项目**不**依赖于 `pytorch`，因此可以**省略**其中的以下部分，**但是**别忘了安装PyTorch外的[依赖包](https://github.com/zhongxinghong/PKUAutoElective#packages)

> 安装 PyTorch，从 PyTorch 官网 中选择合适的条件获得下载命令，然后复制粘贴到命令行中运行即可下载安装。（注：本项目不需要 cuda，当然你可以安装带 gpu 优化的版本）
> 
> ......
> 
> PyTorch 安装时间可能比较长，需耐心等待。
> 如果实在无法安装，可以考虑用其他方式安装 PyTorch，详见附页 PyTorch 安装

## 配置文件

### config.ini

参考 [PKUAutoElective](https://github.com/zhongxinghong/PKUAutoElective#基本用法) 项目中的 `config.ini` 配置说明。

> 由于Python对空格敏感，请确保`[course]`配置部分去除了多余的空格

### apikey.json

**请首先将 apikey.sample.json 复制一份并改名为 apikey.json，并按照以下说明进行配置。**

该文件为 [TT识图](http://www.ttshitu.com) 平台的 API 密钥，在平台注册后，填入用户名与密码即可。由于该 API 需要收费，须在平台充值后方可使用（1 RMB 基本够用 识别一次花费0.002 RMB）。

```json
{
    "username": "xiaoming",
    "password": "xiaominghaoshuai" 
}
```

## 使用说明

### 基本用法

将项目 clone 至本地后，切换至项目根目录下并运行 `main.py` 即可。

```
cd PKUElective2021Spring
python main.py
```

使用 `Ctrl + C` 输送 `KeyboardInterrupt`，可以终止程序运行。

### 高级用法

关于支持的命令行参数，参见 [PKUAutoElective](https://github.com/zhongxinghong/PKUAutoElective#高级用法) 的使用说明。

### 测试识图平台

配置好 `apikey.json` 后，切换至项目根目录，运行`test.py`以测试在线识图是否正常工作

```
python test.py
```

如正常运行，将输出

```
Captcha('vfg8') True
```

## 注意事项

- 请不要使用过低的刷新间隔，过于频繁的访问可能导致IP封禁，建议时间间隔不小于4秒

* 作者可能无视 issue 和 PR，如果您有更好的改进想法，请最好 clone 一份后自行改动
* 请不要在公开场合传播此项目，以免造成不必要的麻烦
* 刷课有风险 USE AT YOUR OWN RISK!

## 致谢

感谢zhongxinhong, Mzhhh, KingOfDeBug等前辈的付出及Totoro-Li对本项目的完善
