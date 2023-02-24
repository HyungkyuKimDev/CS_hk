# conditional statements(条件分岐)

:<<"END"
条件分岐(conditional statements)
1.if文
2.if else文
3.if elif else fi文
4.switch文
END

# if文
:<<"END"
＃条件が[true]の場合、文が実行
if [条件]
then
 A文
fi
END

# 例）　aとbが同じ時、[A and B are same]を出力
a="orange"
b="orange"
if [ $a == $b ]
then
  echo "A and B are same"
fi

# if else文
:<<"END"
#条件が[true]ではない場合、elseの文が実行
if [条件]
then
  A文
else
  B分
fi
END

# 例）　aとbが違う時、[A and B are not same]を出力
b="grape"
if [ $a == $b ]
then 
  echo "A and B are same"
else
  echo "A and B are not same"
fi

# if elif else fi文
:<<"END"
#条件が３つの以上の場合
if [１条件]
then
  A文 
elif [２条件]
then
  B文
  .
  .
  .
else 
  N文
fi
END

# 例） ifの条件（a==b),elifの条件（b==c）、elseの条件(a==c)の場合
c="apple"
if [ $a == $b ]
then
  echo "A and B are same"
elif [ $b == $c ]
then
  echo "B and C are same"
else
  echo "A and C are same"
fi

# swich文
:<<"END"
# caseの引数が値と同じ場合は実行
case [引数] in
  値１） A文 ;;
  値２) B文 ;;
  .
  .
  .
  値N) N文 ;;
esac 
END

#　例）　引数（car)と一致する場合実行
hyundai="car"
case "$hyundai" in
  "car") echo "Hyundai is a car" ;;
  "airplane") echo "Hyundai is a airplane" ;;
  "ship") echo "Hyundai is a ship" ;;
esac
